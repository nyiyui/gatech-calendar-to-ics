# gatech-calendar-to-ics

`./csv_to_ics.py` converts Georgia Tech's Downloadable Academic Calendar to iCalendar (.ics file) format.

[List of Downloadable Academic Calendars](https://registrar.gatech.edu/info/downloadable-academic-calendars)

## Running the Script

If you have [direnv](https://direnv.net/) and [Nix](https://nixos.org/download/) [flakes](https://nixos.wiki/wiki/Flakes) enabled/installed, run `direnv allow`.

Otherwise, install the [ics](https://pypi.org/project/ics/) package (tested using version `0.7.2`).

To run the script itself:
```shell
python3 ./csv_to_ics.py < downloaded_academic_calendar.csv > calendar.ics
```
