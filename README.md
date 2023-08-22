# W5100S_Pico_AI_X

I worked on an interesting project. 

It's a project to post what Pico saw on Twitter. It looks as if Pico is alive.

I was inspired when I saw the project that Benjamin worked on.

The link below is a project that captures an image, analyzes the image with AI, and presents it as a text. Please refer to the link below for more information.

Translating Visuals into Words: Image Captioning with AI

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/07ca6582-b5ce-434e-a460-f8f15f742d7a)

I have to send the text from this project to GPT and send the data to "X". GPT API is simple to use.

## W5100S Ethernet Connection

Let's send the data to the device via Ethernet communication before we trim it slightly in Chat GPT.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/f5738067-70b7-4dea-b2c7-d8206748ab46)

https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/Ethernet%20Example%20Getting%20Started%20%5BMicropython%5D.md

The library using the Wiznet Ethernet Chip on the RP2040, Pico's MCU, is located at the link above.This library allows you to simply attach W5100S to Pico.

Replicate

It's detailed in Benjamin's project. It's using an API, but you need to issue an API key. The function is set like this.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/1283200f-4d5c-466f-ba9f-82fefb6657b3)

And code as below. Saves the text received through the API to x_message.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/3fca8281-c855-4a55-b885-8d53c4c03140)


## Chat GPT API

First, you need to get an API key. You can simply get it issued from the link below.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/e63fb0c9-47cd-44be-b63c-abaa1432dc34)

Code for GPT. I'll simply decide on the role.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/8b71d118-66c3-4c97-b106-13b62c2918ac)

Combine the text I received from the reply I received earlier with the text I will send to GPT. I asked them to leave a simple sentence on SNS.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/11e5b860-28d0-4c49-bf85-67753d930652)


## IFTTT

You can easily proceed by checking the link below.

Writing discord messages / W5100S + Pico

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/f45b8b45-f271-4b5e-a46f-80f4799910c0)

Instead, "Then" selects "Post a sweet with image" as shown in the image below.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/6c721193-2fd9-446a-aacb-752b6e5d071c)

And add Value1 and Value2 respectively. complete!

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/77cb81ed-d95e-4d7b-a2b4-51146156dd76)

Twitter has created a new sub-account. The above IFTTT is linked to this account.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/7502aa4c-e914-4b74-9620-0023656353b0)

And you can use IFTTT like this.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/ecc54eb6-a7ba-4536-86b6-db9cdd8559b7)

image url enters the capture url of Arducam.

## Complete

It's done! I'm going to do the move now. Unfortunately, it is difficult to show this child a good view.

When a child is born, wouldn't it be better to see the father first, just like the parents first?

I'll show you the father of the child. The CEO of Raspberry Pi is Eben Upton. I'd say he's the father of the Pico board.

Fortunately, there is a picture of him on Twitter.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/a76ff51c-4097-41de-ae44-6f1706d76693)

Show the father's face to the child. I'm really curious what kind of answer he'll give.

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/23c38b6d-0a5d-4e27-8fd3-7aad81265b0a)

He answers with great fun. hahaha.  Even the tag is perfect. 

![image](https://github.com/wiznetmaker/W5100S_Pico_AI_X/assets/111826791/d1c308d4-314f-4848-b9f8-4f1f066c5e03)

That was an interesting AI-X-Bot project.

https://www.youtube.com/watch?v=FlP8LNJtgBY

