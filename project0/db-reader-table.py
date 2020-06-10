import csv                              # handle CSV file
import sys

# variables / parameters needed
#print("numargs: ",len(sys.argv))
if len(sys.argv) > 1:
        selection_genre = sys.argv[1] or "ALL"
#        print("setting genre to arg")
else:
        selection_genre = "ALL"
#        print("setting genre to all")
#selection_genre = "ALL"
if selection_genre == 'rnb':
        selection_genre = 'r&b'

### All code below ###
print("<!DOCTYPE html>")
print("<html>")
print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">")
print("<link rel=\"stylesheet\" href=\"style101.css\">")
print("<link rel=\"stylesheet\" href=\"scss101.css\">")

print("<body>")
print("<form><input type=\"button\" value=\"Go back\" onclick=\"history.back()\"></form><br>")

print("<table width=\"100%\" border=\"0\" cellspacing=\"0\">")
print("<tr>")
#
print("<th style=\"width:auto\">Genre</th><th>Album</th>")
print("<th style=\"width:20\">Disc #</th>")
print("<th style=\"width:20\">Track #</th>")
print("<th style=\"width:auto\">Song Title</th>")
print("</tr>")

with open("web-albums.csv") as csv_file:
        #genre, album, disc, track, title in reader:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip first/header row
        next(csv_reader)

        # initialize some vars
        check_genre = "not_set"
        check_album = "not_set"

        # process each following lines
        for row in csv_reader:
                upperGenre = row[0].upper()
                upperSeletction = selection_genre.upper()
                #print("SM=%s, G=%s" %(upperSeletction, upperGenre))
                if upperSeletction == 'ALL' or upperSeletction == upperGenre:
                        #print("genre matched ..")
                        #print("Comparing %s with %s: %s" %(check_genre, row[0], check_genre != row[0]))
                        if check_genre != row[0]:
                        #        print("changed genre ..")
                                check_genre = row[0]
                                if check_genre != 'Genre':
                                        check_album = row[1]
                                        #print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
                                        print(f"<tr><td class=\"genre\" colspan=\"2\"><center>{row[0]}</center></td><td colspan=\"3\"></td></tr>")
                                        print(f"<tr><td class=\"album\" ></td><td colspan=\"4\">{row[1]}</td></tr>")
                                        print(f"<tr><td colspan=\"2\"></td><td style=\"width:auto\">{row[2]}</td>")
                                        print(f"<td style=\"width:auto\">{row[3]}</td>")
                                        print(f"<td>{row[4]}</td>")
                                        print("</tr>")
                        else:
                                print("<tr><td class=\"album\"></td>")
                                print(f"<tr><td colspan=\"2\"></td><td style=\"width:auto\">{row[2]}</td>")
                                print(f"<td style=\"width:auto\">{row[3]}</td>")
                                print(f"<td>{row[4]}</td>")
                                print("</tr>")


print("</table>")

print("</body>")
print("</html>")

