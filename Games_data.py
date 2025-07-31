import requests
from bs4 import BeautifulSoup
import openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Games list"

sheet.append(["Games Names", "Ratings","Genres","Releases Dates","Platforms"])

url="https://opencritic.com/browse/pc"
rr=requests.get(url)
print(rr.status_code)
# print(rr.text)
output=BeautifulSoup(rr.text,"html.parser")

# print(output)

raw_data=output.find("div",class_="mobile-game-display-container")
# print(raw_data)

raw_data2=output.find_all("div",class_="py-2 d-flex mobile-game-display")

games_titles=[]
games_ratings=[]
games_g_p_d=[]
games_data=[games_titles,games_ratings,games_g_p_d]

for i in range(len(raw_data2)):
    movies_titles=raw_data2[i].find_all("div",class_="flex-grow-1 ml-1")
    ratings_data=raw_data2[i].find_all("div",class_="inner-orb small-orb")
    genres_releases_platforms_data=raw_data2[i].find_all("div",class_="mobile-game-info")
    # print(movies_titles)
    # print(ratings_data)
    # print(genres_releases_platforms_data)
#
    for j in range(len(movies_titles)):
        movies_titles2=movies_titles[j].find("strong")
        # print(movies_titles2.text)
        games_titles.append(movies_titles2.text)
        ratings=ratings_data[j].text
        games_ratings.append(ratings)
    genres_releases_platforms_data2=[]

    for k in range(len(genres_releases_platforms_data)):
        # print(genres_releases_platforms_data[k])
        # print(len(genres_releases_platforms_data))
        before_join=genres_releases_platforms_data[k].text
        after_join="".join(before_join)
        genres_releases_platforms_data2.append(after_join)

    games_g_p_d.append(genres_releases_platforms_data2)
    # print(genres_releases_platforms_data2)
    genres_releases_platforms_data2=[]

for i in range(len(games_titles)):

    genres = games_g_p_d[i][0]
    releases = games_g_p_d[i][1]
    platforms = games_g_p_d[i][2]
    print("Games : ",games_titles[i])
    print("Critics : ",games_ratings[i])
    print("Genres : ",genres)
    print("Releases : ",releases)
    print("Platforms : ",platforms)

    sheet.append([games_titles[i], games_ratings[i],genres,releases,platforms])

# print(len(games_titles))
# print(len(games_ratings))
# print(len(games_g_p_d))
# print(len(games_data))
excel.save("Games_Scraping.xlsx")