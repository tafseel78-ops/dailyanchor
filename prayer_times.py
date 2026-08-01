#!/usr/bin/env python3
import urllib.request
import urllib.error
import json

CITY = "Bangalore"
COUNTRY = "India"
METHOD = 1  # University of Islamic Sciences, Karachi - common method for South Asia

def get_prayer_times():
    url = f"https://api.aladhan.com/v1/timingsByCity?city={CITY}&country={COUNTRY}&method={METHOD}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
        return data["data"]["timings"]
    except urllib.error.URLError:
        print("Couldn't reach the prayer times API. Check your internet connection.")
        return None
    except (KeyError, json.JSONDecodeError):
        print("Got a response but couldn't understand it. The API might have changed.")
        return None

def main():
    timings = get_prayer_times()
    if timings is None:
        return
    prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
    print(f"\nToday's prayer times for {CITY}:")
    for prayer in prayers:
        print(f"  {prayer}: {timings[prayer]}")
    print()

if __name__ == "__main__":
    main()
