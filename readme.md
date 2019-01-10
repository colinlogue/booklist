# Booklist

## Purpose
This app will be made to help me keep track of what books and movies I have
seen or read (or listened to - audiobooks and albums as well?) and to record
any thoughts I have about them.

## Actions
The following information-altering actions can be done through this app:
* add a record for a movie/book/whatever
* mark an item for watch list or seen/read/whatever list
* record a note about an item
* tag an item
* apply heirarchical categorization to an item

## Interaction
The following interactions should be enabled by this app:
* See/interact with the wish list and seen/read/whatever list (filter etc.)
* View details of any item's record
* Browse items by tag
* Browse items by category
* Edit an item's record

## Structure
The app will be written in Python as a Flask app, with a MongoDB database.

## Pages
* /
* /wishlist
* /finished
* /browse
* /records/[id]