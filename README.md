## Introduction
> This example of API is based on flask. Using this api you can:
* **create** notes
* **read** notes
* **update** notes
* **delete** notes

Only for [SCoRe Lab](https://codein.withgoogle.com/organizations/score-lab/)

## How to use it?
First, you need to create note:
Send POST request to **http://www.ab2ab.pw:9999/api/create** with next json:

```
{
   name:"note_name",
   description:"note_description"
}
```

Then you can read it. For it use **http://www.ab2ab.pw:9999/api/read?name=notename**, where notename is the name of note, that you created.

Also, you can update the note description. For it you need send POST request to **http://www.ab2ab.pw:9999/api/update** with json:

```
{
   name:"note_name",
   description:"update_note_description"
}
```
And you may delete the note. Use **http://www.ab2ab.pw:9999/api/delete?name=notename**, where notename is the name of the note you want to delete.

If you create a note with a name that already has a note, then you will overwrite it.

## Examples

There is already a finished note on the server with the name of the "note". You can watch it with the httpie utility:

```http GET http://ab2ab.pw:9999/api/read?name=note```

For create note use:

```http POST localhost:9999/api/create name=note description="Hello, SCoRe lab!"```

For delete note use:

```http GET http://ab2ab.pw:9999/api/delete?name=note```

For update note use:

```http POST localhost:9999/api/create name=note description="Hello, SCoRe lab!"```

By Khisaliev