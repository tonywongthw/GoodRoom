# Hack The North 2022

![image of a brightly lit, hostel room with a bunk bed overlooking the view of an apartment window](/marcus-loke-WQJvWU_HZFo-unsplash.jpg) _(Photo by [Marcus Loke](https://unsplash.com/@marcusloke?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))_

## GoodRoom, a voice-powered room servicing platform

![GoodRoom logo](/logo.png)

The story of our project was inspired by a less-than-stellar hotel room service experience involving a ghost call for pillows at 1 AM! 😴 This triggered an idea for us to create an application that integrates with the Telegram API and Voiceflow to enable ease of usability and accessibility when people request room services.

Tech stack:

- [Voiceflow API](https://www.voiceflow.com)
- [Telegram API](https://core.telegram.org)

## Build Setup

```bash
# clone repo
$ git clone `<repo URL>`
```

---

## Table of Contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Screenshots](#screenshots)
  - [Links](#links)
- [Our process](#our-process)
  - [Built with](#built-with)
  - [Further development](#further-development)
  - [Useful resources](#useful-resources)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## Overview

### The challenge

The challenge of this hackathon project was to combine the technologies of Voiceflow and Telegram API.

Some of our following challenges were:

- Whatsapp API is not intuitive to receive messages from. The only way to receive messages was to set up an HTTP server and listen via a webhook, and Whatsapp hadn't simplified the process at all. For the sake of time we decided not to go with Whatsapp and instead used Telegram, which was much simpler.
- dialog response configuration was not easy to set up as we have to learn how to interact with the platform in a very short period of time

Our users would be able to:

- Order room service at any hotel using Goodrooms via Telegram! In the event that room service is not available to take a call and could miss an inquiry, the Goodrooms interface will allow them to register their inquiry with the hotel without the need for anyone to pick up!
- Get information about operating hours of facilities!
- Learn how to place food orders via the hotel interface!

### Screenshots

![Dialog box of Voiceflow chat UI](/dialog-box.png)

_This image displays a sample dialog response and answer feedback loop_

![Response flow chart of Voiceflow dialog design](/response-flow.png)

_Voiceflow\'s web UI showing a visual depiction of the start of a conversation and the resulting flows that arise from different sample answers_

### Links

- [devpost](#)

## Our process

As good developers do, we started off by researching the documentation for Voiceflow and Telegram API. As the hours passed and more snacks were consumed, we ran into nemerous issue that we did not expect.

Eventually, due to configuration issues, we chose to replace a self-developoed front-end web UI to using Telegram API. This helped us maximize quality over quantity.

Our name was created through keyword exploration and logo exploration, based on the keywords of warmth, comfort, room service, and (good) hospitality.

The logo\'s red-violet scheme was chosen to reflect a sense of ambience and night sky colours when a good night\'s sleep was had. The colour range sits between the vibrance of warm colours (yellows, oranges) and the seriousness of darker, cold colours.

### Built with

Built with Voiceflow API and Telegram API.

### Further development

Given our original intention was to create an application that was field-agnostic, we hope to expand this project\'s use-cases to pharmacy and telehealth.

### Useful Resources

- [Voiceflow API documentation](https://www.voiceflow.com/docs)
- [Telegram API documentation](https://core.telegram.org)

## Authors

- [@serhatgktp](https://github.com/serhatgktp)
- [@tonywongthw](https://github.com/tonywongthw)
- [@maureento8888](https://github.com/maureento8888)

## Acknowledgements

- BIG THANK YOU to [Hack the North](https://hackthenorth.com) 2022!
- LOTS of appreciation for the sponsors, volunteers, and staff members who pulled off a great success! 🎉🧑🏻‍💻
