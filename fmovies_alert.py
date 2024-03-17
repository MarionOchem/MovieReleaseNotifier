import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SCRAP CONFIG 
movie_search = "" # movie-title (string matching the webstite URL typography for movie titles in a /search HTTP request)
movie_title = "" # Movie title 
url = "https://fmovies.ps/search/" + movie_search


# SEND EMAIL 
def send_email(body):
    # Email config
    sender_email = "" 
    receiver_email = "" 
    password = "" # The app password for your email service account, used for accessing your email through a third-party app
    subject = "Match Found"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Establish SMTP connection and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# SCRAPING 
def scrape_website(url):

    # Send th HTTP GET request to the targeted website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the html content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the <a> tag containing the movie title
        check = soup.find("a", {"title": movie_title})
        if check:
            # Check if the movie quality is "HD"
            quality = check.find_previous_sibling("div", class_="pick film-poster-quality")
            if quality and quality.text.strip() == "HD":
                # Send an email notification with the movie's URL
                send_email("Your movie is available at :  " + "https://fmovies.ps" + check.get('href'))            
    else:
        print("Failed to fetch website:", response.status_code)
        return None    



scrape_website(url)


