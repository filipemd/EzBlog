# EzBlog
EzBlog is an application, currently in beta version, made in Flask to make it easier for people to create their own blog. It wasn't made for those who don't have knowledge of Flask and HTML, but for those who already know.

It works simply. There is a file called `info.json`, where you will place your blog information.

Structure:

```
{
    "blog-name" : "[blog name]"
}
```

There is also a folder called `articles` where you will create other folders. Inside these folders, you will place a file called `index.md`. In the future, it will be possible to write articles using HTML instead of Markdown.

You will also add another file called `info.json`, where you will place the article information.

Structure:

```
{
    "number": [the descending order in which the articles will appear],
    "title" : "[title of the article]",
    "date" : "[the date where the article was written]",
    "writer" : "[who wrote the article]",
    "description" : "[the description of the article]"
}
```

File structure:

```
.
├── app.py
├── articles
│ ├── Article
│ │ ├── index.md
│ │ └── info.json
│ └── Other Article
│ ├── index.md
│ └── info.json
├── info.json
├── static
│ └── css
│ └── style.css
└── templates
    ├── article.html
    └── index.html
```

Ideally, you should modify the CSS, HTML and even the back-end of the code.
