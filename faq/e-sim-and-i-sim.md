## eSIM and iSIM

### What is an eSIM/iSIM?

The term **eSIM** is used in two different ways, which often causes confusion:

- **eSIM as a form factor (MFF2)**
- **eSIM as a reprogrammable SIM with loadable profiles (GSMA eUICC)**

In the context of the **form factor**, eSIM simply means a **soldered SIM chip** mounted on the PCB 
instead of a removable plastic SIM card.

- Form factor name: **MFF2**
- It behaves exactly like a traditional SIM card.
- It contains **one fixed profile**, written once by the operator.
- It is **not** reprogrammable by the user.

People sometimes call this “eSIM” because it’s *embedded*, but technically it’s just a normal SIM in
a different package.

In the other case, eSIM refers to **GSMA eUICC technology**, which allows the SIM to hold multiple 
operator profiles that can be downloaded, activated, or deleted over the air.

Key characteristics:

- Based on the **eUICC** architecture (embedded Universal Integrated Circuit Card).
- Supports **Remote SIM Provisioning (RSP)**.
- Allows switching operators without physically replacing hardware.
- Hardware form factors supporting eUICC:
  - **MFF2 (soldered) eUICC**
  - **2FF/3FF/4FF plastic eUICC SIM cards**
  - **iSIM** (integrated inside the cellular modem)

### Does Walter support eSIM technology?

As Walter focuses on low- to medium-volume products, we have chosen to support the 
**4FF physical SIM card** form factor and not solder an MFF2 SIM on-board. This gives our users 
complete flexibility in choosing the SIM hardware and operator they want to work with.

The modem **does** support eUICC functionality, and you can perfectly use a SIM card with 
reprogrammable or multiple profiles with Walter. The official statement from Sequans about eSIM 
support on the GM02SP modem in Walter, as of **25 November 2025**, is as follows:

> - Our modules are interoperable with MNOs/MVNOs’ SGP.21/SGP.32 SIM, eSIM (plastic, MFF2) whose  
>   SIM OS are Kigen or Thales  
> - Also both Kigen and Thales have their own SGP.32 SIM/eSIM offering including the SIM  
>   management platform for customers  
> - Tools for customers will be available beginning of next year for downloading profiles in their  
>   production line (does not require a secure GSMA environment)

### Does Walter contain an iSIM?

The modem in Walter, the **Sequans GM02SP**, contains iSIM hardware. At this point in time, the iSIM
hardware is **not activated** by our supplier Sequans. As soon as Sequans provides any update
concerning iSIM availability on the modem, we will announce it.