# Project 0

Web Programming with Python and JavaScript

This project will catalog and display my iTunes music library. It will pull the
data from CSV file and display on webpages based on the selected genre or display
all the songs grouped by genre.

The content frame will present the list of all available genres of the music in
my catalog. Based on user selection the list of songs will be displayed in the
"body" frame, grouped by the album.

index   - base file that contains the frames for header, contents and body
head    - simply displays the 'domain' graphic
content - list all the genres from the itunes library
songs   - list all the songs based on the selected genre, or "All"

REQUIREMENTS:
- four different html files included as base files, plus the song list html's
  include a back button
- the content view uses a unordered list to provide links to the different music
  genres
- a table was used for the single genre's while the bootstrap grid model was used
  for the "All" view.
- SCSS and CSS files merged
- image used in the header
- border style attributes, font color and background color as defined as variables
- five different types of CSS selectors =
        img, body, table header (th), unsorted list, @media, #id's
- five different CSS properties
        color, display, border-radius, background-color, font-color,
        border, border-style, border-widthborder-color
- the #id selector used
        #blinker - content genre list, blinks
        #all_music -
        #all_music_text -
- the .class selector used
        "All" genre div grid, .col, .col-2, .col-3, .col-4, .col-5

NOTE:
For this particular design, I cannot see how to add the SCSS inheritance.
The examples i've been finding all look at the success/warning/failure event,
which don't apply to my site.

