"""
Comprehensive Demonstration of Network & API Calling Functionalities in Python
-------------------------------------------------------------------------------
This module demonstrates key networking concepts, REST API interaction, and HTTP handling in Python:

1. Standard Library (`urllib.request`) vs High-Level (`requests`) Client
2. HTTP Methods (GET, POST, PUT, DELETE) & Payload Encoding (JSON)
3. Robust Error Handling (Timeouts, HTTP Errors, Connection Failures)
4. Network Concurrency (Parallel Requests using `concurrent.futures.ThreadPoolExecutor`)
5. Custom Retry Logic with Exponential Backoff
6. Object-Oriented Client Architecture & Type Annotations

APIs Used (Free, Open Access, No API Key Required):
- Open-Meteo API: Real-time global weather data
- JSONPlaceholder API: Mock REST API for CRUD operations
"""

import time
import json
import urllib.request
import urllib.error
import warnings
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress LibreSSL vs OpenSSL warning on macOS Python 3.9
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL.*")
import requests


# ==========================================
# 1. DATA MODELS (Type-Safe API Responses)
# ==========================================
@dataclass
class CityCoordinates:
    """Geographic coordinates for weather API lookup."""
    name: str
    latitude: float
    longitude: float


@dataclass
class WeatherReport:
    """Structured representation of API weather payload."""
    city: str
    temperature_c: float
    wind_speed_kmh: float
    weather_code: int
    is_day: bool
    timestamp: str

    @property
    def temperature_f(self) -> float:
        """Helper property to calculate Fahrenheit."""
        return round((self.temperature_c * 9 / 5) + 32, 1)

    def __str__(self) -> str:
        day_night = "Day ☀️" if self.is_day else "Night 🌙"
        return (f"{self.city:<12} | {self.temperature_c:>5.1f}°C ({self.temperature_f:>5.1f}°F) | "
                f"Wind: {self.wind_speed_kmh:>5.1f} km/h | {day_night}")


# ==========================================
# 2. STANDARD LIBRARY DEMO (urllib.request)
# ==========================================
def fetch_ip_with_urllib() -> Dict[str, Any]:
    """
    Demonstrates HTTP GET using Python's built-in `urllib.request` module.
    Useful when external dependencies like `requests` are not available.
    """
    urls = ["https://api.ipify.org?format=json", "https://httpbin.org/ip"]
    headers = {"User-Agent": "Python-Network-Demo/1.0"}

    for url in urls:
        req = urllib.request.Request(url, headers=headers)
        try:
            # Perform network call with a strict 5-second timeout
            with urllib.request.urlopen(req, timeout=5) as response:
                status_code = response.getcode()
                raw_data = response.read().decode('utf-8')
                json_data = json.loads(raw_data)
                return {"status": status_code, "data": json_data}
        except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError):
            continue

    return {"error": "Failed to fetch public IP from available services"}


# ==========================================
# 3. ADVANCED REST CLIENT (requests library)
# ==========================================
class WeatherAPIClient:
    """
    Client for interacting with Open-Meteo REST API.
    Demonstrates sessions, parameters, timeouts, and exception handling.
    """

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, timeout: float = 5.0, max_retries: int = 3):
        self.timeout = timeout
        self.max_retries = max_retries
        # Use requests.Session for connection pooling and header reuse
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Python-API-Demo/1.0",
            "Accept": "application/json"
        })

    def get_weather(self, city: CityCoordinates) -> WeatherReport:
        """
        Fetches current weather for a city with retry logic and error handling.
        """
        params = {
            "latitude": city.latitude,
            "longitude": city.longitude,
            "current_weather": "true"
        }

        last_exception = None
        for attempt in range(1, self.max_retries + 1):
            try:
                # Perform HTTP GET request
                response = self.session.get(self.BASE_URL, params=params, timeout=self.timeout)
                
                # Raise HTTPError if status is 4xx or 5xx
                response.raise_for_status()

                data = response.json()
                current = data.get("current_weather", {})

                return WeatherReport(
                    city=city.name,
                    temperature_c=float(current.get("temperature", 0.0)),
                    wind_speed_kmh=float(current.get("windspeed", 0.0)),
                    weather_code=int(current.get("weathercode", 0)),
                    is_day=bool(current.get("is_day", 1)),
                    timestamp=str(current.get("time", ""))
                )

            except requests.exceptions.Timeout as err:
                last_exception = f"Timeout on attempt {attempt}: {err}"
            except requests.exceptions.HTTPError as err:
                last_exception = f"HTTP Error on attempt {attempt}: {err}"
            except requests.exceptions.RequestException as err:
                last_exception = f"Network Error on attempt {attempt}: {err}"

            # Exponential backoff delay before retrying
            time.sleep(0.5 * (2 ** (attempt - 1)))

        raise RuntimeError(f"Failed to fetch weather for {city.name} after {self.max_retries} attempts. Last error: {last_exception}")

    def get_multiple_cities_parallel(self, cities: List[CityCoordinates]) -> List[WeatherReport]:
        """
        Demonstrates NETWORK CONCURRENCY using ThreadPoolExecutor.
        Fetches multiple API endpoints concurrently in parallel threads.
        """
        reports: List[WeatherReport] = []
        
        # Spawn thread pool matching number of cities (up to 10 threads)
        with ThreadPoolExecutor(max_workers=min(len(cities), 10)) as executor:
            # Map futures to city objects
            future_to_city = {executor.submit(self.get_weather, city): city for city in cities}
            
            for future in as_completed(future_to_city):
                city = future_to_city[future]
                try:
                    report = future.result()
                    reports.append(report)
                except Exception as exc:
                    print(f"  ❌ Error fetching weather for {city.name}: {exc}")

        return reports


# ==========================================
# 4. HTTP VERBS DEMO (REST CRUD Operations)
# ==========================================
class RestCRUDDemoClient:
    """
    Demonstrates HTTP GET, POST, PUT, DELETE verbs using JSONPlaceholder mock API.
    """

    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json; charset=UTF-8"})

    def create_post(self, title: str, body: str, user_id: int) -> Dict[str, Any]:
        """Demonstrates HTTP POST with JSON body payload."""
        payload = {"title": title, "body": body, "userId": user_id}
        response = self.session.post(self.BASE_URL, json=payload, timeout=5)
        response.raise_for_status()
        return {"status_code": response.status_code, "data": response.json()}

    def update_post(self, post_id: int, title: str, body: str, user_id: int) -> Dict[str, Any]:
        """Demonstrates HTTP PUT (full resource update)."""
        url = f"{self.BASE_URL}/{post_id}"
        payload = {"id": post_id, "title": title, "body": body, "userId": user_id}
        response = self.session.put(url, json=payload, timeout=5)
        response.raise_for_status()
        return {"status_code": response.status_code, "data": response.json()}

    def delete_post(self, post_id: int) -> Dict[str, Any]:
        """Demonstrates HTTP DELETE."""
        url = f"{self.BASE_URL}/{post_id}"
        response = self.session.delete(url, timeout=5)
        response.raise_for_status()
        return {"status_code": response.status_code, "message": f"Post {post_id} deleted successfully."}


# ==========================================
# 5. EXECUTION AND BENCHMARKING SCRIPT
# ==========================================
def main():
    print("=" * 75)
    print("      PYTHON API CALLING & NETWORK FUNCTIONALITIES DEMONSTRATION      ")
    print("=" * 75)

    # ---------------------------------------------------------
    # PART 1: Standard Library (urllib)
    # ---------------------------------------------------------
    print("\n1. STANDARD LIBRARY (urllib.request) HTTP GET")
    print("-" * 50)
    print("Fetching public IP using built-in urllib.request...")
    ip_result = fetch_ip_with_urllib()
    print(f"Result: {ip_result}")

    # ---------------------------------------------------------
    # PART 2: REST Weather API & Parallel Fetching
    # ---------------------------------------------------------
    print("\n2. REST API & PARALLEL NETWORK CONCURRENCY (Open-Meteo Weather)")
    print("-" * 50)
    cities = [
        CityCoordinates("Tokyo", 35.6762, 139.6503),
        CityCoordinates("London", 51.5074, -0.1278),
        CityCoordinates("New York", 40.7128, -74.0060),
        CityCoordinates("Paris", 48.8566, 2.3522),
        CityCoordinates("Sydney", -33.8688, 151.2093),
        CityCoordinates("Manila", 14.5995, 120.9842),
    ]

    weather_client = WeatherAPIClient(timeout=5.0)

    # Sequential Benchmark
    print("Fetching weather sequentially...")
    start_seq = time.time()
    seq_reports = [weather_client.get_weather(city) for city in cities]
    seq_duration = time.time() - start_seq
    print(f"  Finished sequential requests in {seq_duration:.2f} seconds.")

    # Parallel Benchmark using ThreadPoolExecutor
    print("\nFetching weather concurrently using ThreadPoolExecutor...")
    start_par = time.time()
    par_reports = weather_client.get_multiple_cities_parallel(cities)
    par_duration = time.time() - start_par
    print(f"  Finished parallel requests in {par_duration:.2f} seconds.")

    # Speedup calculation
    speedup = (seq_duration / par_duration) if par_duration > 0 else 1.0
    print(f"  🚀 Concurrency Speedup: {speedup:.2f}x faster!")

    print("\n--- Live Global Weather Roster ---")
    for report in sorted(par_reports, key=lambda r: r.city):
        print(f"  * {report}")

    # ---------------------------------------------------------
    # PART 3: HTTP Verbs (POST, PUT, DELETE)
    # ---------------------------------------------------------
    print("\n3. HTTP VERBS & REST CRUD OPERATIONS (JSONPlaceholder API)")
    print("-" * 50)
    crud_client = RestCRUDDemoClient()

    # POST
    print("Sending HTTP POST (Create Resource)...")
    post_res = crud_client.create_post("OOP Python Guide", "Learn classes, APIs, and network programming.", user_id=1)
    print(f"  Status Code: {post_res['status_code']}")
    print(f"  Response JSON: {post_res['data']}")

    # PUT
    print("\nSending HTTP PUT (Update Resource #1)...")
    put_res = crud_client.update_post(1, "Updated Title", "Updated post body content.", user_id=1)
    print(f"  Status Code: {put_res['status_code']}")
    print(f"  Response JSON: {put_res['data']}")

    # DELETE
    print("\nSending HTTP DELETE (Remove Resource #1)...")
    del_res = crud_client.delete_post(1)
    print(f"  Status Code: {del_res['status_code']}")
    print(f"  Response Message: {del_res['message']}")

    # ---------------------------------------------------------
    # PART 4: Error Handling & Resilience Demo
    # ---------------------------------------------------------
    print("\n4. NETWORK ERROR HANDLING & TIMEOUT RESILIENCE")
    print("-" * 50)
    print("Testing connection timeout handling (0.001 sec timeout)...")
    try:
        requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": 0, "longitude": 0}, timeout=0.001)
    except requests.exceptions.Timeout as err:
        print(f"  ✅ Caught expected Timeout Exception: {type(err).__name__}")

    print("Testing HTTP 404 error handling...")
    try:
        res = requests.get("https://jsonplaceholder.typicode.com/invalid_endpoint_404")
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"  ✅ Caught expected HTTPError (Status Code {err.response.status_code}): {err}")

    print("\n" + "=" * 75)
    print("               ALL NETWORK & API DEMONSTRATIONS COMPLETED               ")
    print("=" * 75)


if __name__ == "__main__":
    main()
