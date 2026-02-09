---
marp: true
theme: beam
paginate: true
style: |
  h1 {
    position: absolute;
    top: 60px;
    left: 75px;
    right: 75px;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
header: 'The Cloud'
footer: '© 2026 Computacenter PSCP All Rights Reserved'

---

# The Cloud
Anthony Farina
DevOps Engineer
Computacenter - Professional Services Consultancy Practice

---

# What is "The Cloud"?
<div class="columns">
<div>

- The on-demand access to server resources at datacenters
  - A single datacenter is made up of 100's if not 1,000's of servers
- Allows you to use digital services provided by companies
  - You don't need to download software to use services
- Examples: Netflix, Google Drive, ChatGPT

</div>
<div>

![w:600 h:200](./assets/google_datacenter.png)
![w:600 h:300](./assets/the_cloud.png)

</div>
</div>

---

# NVIDIA Tesla V100 vs. Raspberry Pi
<div class="columns">
<div>

![](./assets/nvidia_v100.jpg)
- Uses its own resources
- 640 Tensor Cores
- 32 GB RAM

</div>
<div>

![](./assets/raspberry_pi_5.webp)

- Integrated graphics (no physical GPU)
- 4 CPU cores
- At most 16 GB RAM

</div>

---

# Simulating the Cloud Using 2 Pi's
<div class="columns">
<div>

![](./assets/raspberry_pi_5.webp)

- A user will make a prompt on this pi and it will send that prompt to the other pi
------------------------------------->

</div>
<div>

![](./assets/raspberry_pi_5.webp)

- This pi will recieve the prompt, run an Ollama AI model, generate a response, and send it back to the first pi
<-------------------------------------

</div>

---

# Using the Real Cloud
<div class="columns">
<div>

- Rich set up a V100 in the Cloud for us to use!
- The AI model we'll be using is DeepSeek-R1
- DeepSeek is an LLM development company based out of China

</div>
<div>

![](./assets/nvidia_v100.jpg)

</div>
