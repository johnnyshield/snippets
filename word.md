# Word

## Word - chapter number in numbered list
There's no way to do this directly as you can't include fields as prefixes to multi-level lists. However, you can use SEQ numbering: https://gregmaxey.com/word_tip_pages/seq_field_numbering.html and combine it with chapter code.

![image](https://user-images.githubusercontent.com/36623114/188940182-d6069564-e3fd-48cb-b0cd-6a1a412bb592.png)

```
{ STYLEREF 2 \s }.{ SEQ A \r1 } Use at start of new list - restarts at 1
{ STYLEREF 2 \s }.{ SEQ A }     Next line etc.
```
Use CTRL+F9 to insert field instead of typing curly brackets.
Note that these won't update automatically if you move lines up or down, use CTRL+A, F9 to update all fields.

![image](https://user-images.githubusercontent.com/36623114/188940303-b9fe7742-78bc-4c63-a1da-ff7b54c45ed1.png)
