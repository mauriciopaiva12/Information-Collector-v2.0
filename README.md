# Information Collector v2.1
 
<p>

__*Project dedicated to collecting information in the first stages of a Pentest.<br />
The project is not yet finalized, as I am evolving over time, so I will still receive several updates.*__

<p>

---

## Required libraries and facilities

<p>

Some libraries are needed, such as: socket, sys, time.<br />
To install them, just copy and paste the following codes into the terminal, remembering that each version of the pip corresponds to a version of python.<br />

<p>

---

### Installation

`pip3 install sockets`

---

## What is in the project and what will be implemented?

<p>
 
In the list below it will be possible to view everything that currently exists in the project and everything that I intend to implement currently.<br />

</p>

---

### What exists and what will come:

 - [x] PortScan.<br />
 - [x] DNS brute force<br />
 - [ ] Domain folder discovery<br />
 - [ ] You can save the output<br />
 
---

## PortScan category and full category

<p>
 
*Next, I'll talk a little bit about the categories, both the portscan category and the full category, I'll talk a little bit about how it works and about planning.*

</p>

---

### PortScan

<p>
 
Within the PortScan category it is possible to do two types of scans, one with the main ports and the other complete.<br /><br />
The scan with the main doors presents the open and closed doors of the desired destination, but both are differentiated by colors.<br />
In full scan, it scans all the target's ports, but with a differential from the other, it presents only the open ports.

</p>

---

### Complete Category

<p>

The full category contains Brute Force DNS and a PortScan, with PortScan scanning only the main ports. PortScan differentiates between open and closed doors by color, whereas the Brute Force DNS brings only positive responses.

<p>

---

### Planning

<p>
 
 As the construction of the Brute Force DNS has been completed, I will start the construction of a domain directory discovery system.
 
</p>
