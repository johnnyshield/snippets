# Snippets
Scraps of useful code and scripts


## PowerPoint VBA clone or duplicate animations
```
Sub clone_animations()
Dim s As Slide
Dim i As Integer
' Ensure current slide is selected
Set s = Application.ActiveWindow.View.Slide
' Code in animations you want to clone
' Apparently not possible to access "selected animation" in vba
For i = 8 To 11
s.TimeLine.MainSequence.Clone s.TimeLine.MainSequence(i)
Next
End Sub
```

## Excel - cumulative sum in table
```
=SUM(INDEX([ColName],1):[@ColName])
```

## Word - chapter number in numbered list
There's no way to do this directly as you can't include fields as prefixes to multi-level lists. However, you can use SEQ numbering: https://gregmaxey.com/word_tip_pages/seq_field_numbering.html and combine ith with chapter code.

![image](https://user-images.githubusercontent.com/36623114/188940182-d6069564-e3fd-48cb-b0cd-6a1a412bb592.png)

```
{ STYLEREF 2 \s }.{ SEQ A \r1 } Use at start of new list - restarts at 1
{ STYLEREF 2 \s }.{ SEQ A }     Next line etc.
```
Use CTRL+F9 to insert field instead of typing curly brackets.
![image](https://user-images.githubusercontent.com/36623114/188940303-b9fe7742-78bc-4c63-a1da-ff7b54c45ed1.png)
