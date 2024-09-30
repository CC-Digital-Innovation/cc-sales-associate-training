---
marp: true
theme: beam
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
paginate: true
header: 'Presentation Tile'
footer: '© 2024 Computacenter Digital Innovation  All Rights Reserved'

---
<!-- _class: title -->
# Presentation Title
Author
Organization
Session Name

<!--
** Slide Notes
-->

---
# Agenda
<div style='margin-top:60px'></div>
<div class="columns">
<div>


- Item one
- Item two
- Item three

</div>
<div>

![](./assets/image.jpg)

</div>
</div>

<!--
** Slide Notes
-->

---
# Alt Agenda / Topics Slide
<div class="columns">
<div>
<div style='margin-top:30px'></div>

- Item one
- Item two
- Item three


</div>
<div>
<img src="./assets/image.jpg" alt="Agenda">

</div>
</div>

<!--
** Slide Notes
-->

---
# Basic Text Slide
## Heading
- Text
- Text
### Heading 2
- Text
  - Text

---
# Code Slide
## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

- We create a greeting function
- The function is named `greet` and it accepts the `name` argument
- The function returns a greeting message back to the caller

<!--
Notes:
`def` - defines the function
`greet` - is the name of the function
`(name)` - is where the parameters of the function are placed. Don't forget scope!
`return` - sends a value back to the caller of the function
-->

---
# Side by Side Code and Image Slide
<div class="columns">
<div>

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

- We create a greeting function
- The function is named `greet` and it accepts the `name` argument
- The function returns a greeting message back to the caller


</div>
<div>

<br><br>
<center><img src="./assets/image.jpg" alt="Image" height="400"></center>

</div>
</div>


<!--
** Slide Notes
-->

---
# Quote Slide
<b>Subtitle</b>
<hr>
<center>“Blah, blah, blah...” </center>
<hr>
<center>Author</center>

<!--
** Slide Notes
-->

---
# Image Slide
![bg 60%](./assets/image.jpg)

<!--
** Slide Notes
-->

---
# Alt Image Slide
<div style='margin-top:70px'></div>
<center><img src="./assets/image.jpg" alt="Image" height="600"></center>

<!--
** Slide Notes
-->


---
# Side by Side Images
![bg 90%](./assets/image.jpg)
![bg 90%](./assets/image.jpg)

<!--
** Slide Notes
-->

---
# Alt Side by Side Images
## Subtitle
<div class="columns">
<div>


![w:600 h:420](./assets/image.jpg)
</div>
<div>


![w:600 h:420](./assets/image.jpg)
</div>
</div>

<!--
** Slide Notes
-->




---
# Side by Side Text
<div class="columns">
<div>

## Heading
- Item one
- Item two
- Item three

</div>
<div>

## Heading
- Item one
- Item two
- Item three

</div>
</div>

<!--
** Slide Notes
-->





---
# Side by Side Quote and Image
<div class="columns">
<div>
<div style='margin-top:70px'></div>
<hr>
<center>"Blah, blah, blah..."
<hr>
Author</center>

</div>
<div>

![](./assets/image.jpg)

</div>
</div>

<!--
** Slide Notes
-->


---
# Side by Side Text and Image
<b>Heading</b>
<div class="columns">
<div>

- Item one
- Item two
- Item three

</div>
<div>

![](./assets/image.jpg)

</div>
</div>


<!--
** Slide Notes
-->


---
# Video Slide
<div style='margin-top:70px'></div>
<center><video controls="controls" width=1024 src="./assets/video.mp4"></video></center>


<!--
** Slide Notes
-->

---
# Side by Side Video

<div style='margin-top:70px'></div>
<div class="columns">
<div>
<b>Title</b>
<center><video controls="controls" width=100% src="./assets/video.mp4"></video></center>
</div>

<div>
<b>Title</b>
<center><video controls="controls" width=100% src="./assets/video.mp4"></video></center>

</div>
</div>

<!--
** Slide Notes
-->



