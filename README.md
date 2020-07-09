# Wiki
Designing a Wikipedia-like online encyclopedia using Django & HTML.

## Understanding

In practice, it would start to get tedious if every page on Wikipedia had to be written in HTML. 

Instead, it can be helpful to store encyclopedia entries using a lighter-weight human-friendly markup language. 

Wikipedia happens to use a markup language called Wikitext, but for this project to store encyclopedia entries I've used the very popular markup language called Markdown.

Each encyclopedia entry will be saved as a Markdown file inside of the entries/ directory. While rendering each page, it is then converted into HTML. 

## Features
- Index page 
- Search bar 
- New page
- Edit page
- Random page
