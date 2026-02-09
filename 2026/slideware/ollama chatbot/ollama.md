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
header: 'IO, constants, and variables'
footer: '© 2024 Computacenter Digital Innovation  All Rights Reserved'

---
<!-- _class: title -->
# Simple Chatbot with Ollama
Ben Verley
Computacenter

<!--
** Slide Notes
-->

---
# Agenda
<div style='margin-top:60px'></div>
<div class="columns">
<div>


- Ollama what is it
- Models
- Lets work with it

</div>
</div>

<!--
** Slide Notes
-->


---


# Ollama

<div class="columns">
<div>

Ollama is an open source platform that you can develope AI solutions with most models. Hosted either in the cloud or on local hardware.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

</div>
<div>


<center><img src="../images/ollama-logo.png" alt="Image"></center>

</div>
</div>


<!--
** Slide Notes
-->


---

# Models
We can run sessions with different models straight from the command line. The bigger the model we want to use the longer it will take to pull and run.

- ollama pull {model name} 
- ollamma run {model name}

<!--
Notes:
-->
---
# Models Continued
There are many to choose from, we have preloaded some models that should* run on the Pis for use in this session

- tinyllama - A 1 billion parameter model from Ollama
- Gemma:4B - a 4 Billion parameter version of Google's open source model
- Deepseek:8B - an 8 Billion parameter version of deepseek

<!--
Notes:
-->

---
the CLI is great, but we will need more control over inputs and outputs if we want to build something more than just a chatbot... with that

# Lets Build!











