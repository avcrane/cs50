import csv                              # handle CSV file
import sys

# variables / parameters needed
#print("numargs: ",len(sys.argv))
if len(sys.argv) > 1:
        #print("setting genre to arg")
        selection_genre = sys.argv[1]
else:
        #print("setting genre to all")
        selection_genre = "ALL"
# redefine selection R&B as it's harder to pass via CLI
if selection_genre == 'rnb':
        selection_genre = 'r&b'

### All code below ###
print("<!DOCTYPE html>")
print("<html>")
print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">")
print("<link rel=\"stylesheet\" href=\"style101.css\">")
print("<link rel=\"stylesheet\" href=\"scss101.css\">")
#
print("<body>")
print("<form><input type=\"button\" value=\"Go back\" onclick=\"history.back()\"></form><br>")
print("<tr>")
#
print("<meta charset=\"utf-8\">")
print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
#
###
#print("<table width=\"100%\" border=\"0\" cellspacing=\"0\">")
#print("<tr>")
#print("<th style=\"width:auto\">Genre</th><th>Album</th>")
#print("<th style=\"width:20\">Disc #</th>")
#print("<th style=\"width:20\">Track #</th>")
#print("<th style=\"width:auto\">Song Title</th>")
#print("</tr>")
#print("</table>")
###
print("<div class=\"container-fluid\" id=\"all_music\">")
print("<div class=\"row\" id=\"all_music_text\">")
print("<div class=\"col-2\" style=\"test-align: center;\">Genre</div>")
print("<div class=\"col-3\">Album</div>")
print("<div class=\"col\">Disc</div>")
print("<div class=\"col\">Track</div>")
print("<div class=\"col-5\">Title</div>")
print("</div>")

with open("web-albums.csv") as csv_file:
        #genre, album, disc, track, title in reader:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip first/header row
        next(csv_reader)

        # initialize some vars
        check_genre = "not_set"
        #check_album = "not_set"

        # process each following lines
        for csv_row in csv_reader:
                upperGenre = csv_row[0].upper()
                upperSeletction = selection_genre.upper()
                #print(f"SM=%s, G=%s" %(upperSeletction, upperGenre))
                if upperSeletction == 'ALL' or upperSeletction == upperGenre:
                        #print("Comparing %s with %s: %s" %(check_genre, row[0], check_genre != row[0]))
                        if check_genre != csv_row[0]:
                                check_genre = csv_row[0]
                                if check_genre != 'Genre':
                                        #print("changed genre ..")
                                        #check_album = csv_row[1]
                                        #print(f"{csv_row[0]} | {csv_row[1]} | {csv_row[2]} | {csv_row[3]} | {csv_row[4]}")

                                        print("<div class=\"row\">")
                                        print(f"<div class=\"col-3\" style=\"text-align: left;\">{csv_row[0]}</div>")
                                        print("<div class=\"col-9\"></div>")
                                        print("</div>")

                                        print("<div class=\"row\">")
                                        print("<div class=\"col-3\"></div>")
                                        print(f"<div class=\"col-4\">{csv_row[1]}</div>")
                                        print("<div class=\"col-5\"></div>")
                                        print("</div>")

                                        print("<div class=\"row\">")
                                        print("<div class=\"col-5\"></div>")
                                        print(f"<div class=\"col\">{csv_row[2]}</div>")
                                        print(f"<div class=\"col\">{csv_row[3]}</div>")
                                        print(f"<div class=\"col-5\">{csv_row[4]}</div>")
                                        print("</div>")
                        else:
                                #print("genre matched ..")
                                print("<div class=\"row\">")
                                print("<div class=\"col-5\"></div>")
                                print(f"<div class=\"col\">{csv_row[2]}</div>")
                                print(f"<div class=\"col\">{csv_row[3]}</div>")
                                print(f"<div class=\"col-5\">{csv_row[4]}</div>")
                                print("</div>")
print("</div>")

print("</body>")
print("</html>")

