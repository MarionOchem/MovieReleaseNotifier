# MovieReleaseNotifier

Automating the tracking and notifying of a chosen film release on the Fmovies streaming website.

Web scraping script in python scanning a targeted website for the release of a particular film. When a release occurs, the script automatically sends an email notification.
This is achieved through a combination of python scripts and shell scripts, orchestrated by scheduled cron jobs.
This project is tailored for execution within a Linux server environment.

## Use :

- Provide the details of the target movie and the email account (fmovies_alert.py)
- Create a virtual environment in the project directory
- Edit the file paths according to your project directory (fmovies_alert_script.sh)
- Set up a cronjob

## Tools :

- Python
- requests
- BeautifulSoup
- smtplib
- Bash
- crontab
- Google App Password
