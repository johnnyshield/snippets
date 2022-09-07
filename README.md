# Snippets
Scraps of useful code and scripts


## PowerPoint VBA clone or duplicate animations
```
Sub clone_animations()
Dim s As Slide
Dim i As Integer
'Ensure current slide is selected
Set s = Application.ActiveWindow.View.Slide
'Select animations you want to clone
For i = 8 To 11
s.TimeLine.MainSequence.Clone s.TimeLine.MainSequence(i)
Next
End Sub
```

## Excel - cumulative sum in table
```
=SUM(INDEX([ColName],1):[@ColName])
```
