# Powerpoint

## VBA clone or duplicate animations
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
