# Pi Pico Black Box

tl;dr - box that tracks gps data and saves it for you to consult later.

<img width="589" height="786" alt="image" src="https://github.com/user-attachments/assets/2d1656b7-b3a4-4f2f-803b-aca81854bb1d" />


So thanks to the fact that a free CubeSat camp I signed up for a couple years ago never ran, I realized I had a bunch of hardware lying around in my closet! This included a Pi Pico, a MikroBus Click Shield, and many sensors. Since I saw GPS, I decided it would be interesting to make something similar to a plane's black box.

# What's a black box?
Black boxes track a lot of data about planes so they can be consulted in the event of a crash. This can include a lot of voice, telemetery, location, and other data. This project just tracks location for up to around 5 and a half hours (after that, it deletes the oldest info in order to add new info).

# How does this work?
By using the micropyGPS package, I'm able to sort the NASM-formatted data that the GPS connected to the Pi gives me into much more readable data, which is then written to files. There are 3 files, one for latitude, one for longitude, and one for altitude.

# Why does this matter?
This project more than anything is a proof of concept. As I don't have access to a Pi with wireless capabilites currently, I'm not able to build a tracker, so instead I'm building everything I would need for one.

# Future Ideas
I may add speed information with a gyro sensor that the kit also had. I also have a case in the process of being 3D printed, which looks like this:

<img width="553" height="586" alt="image" src="https://github.com/user-attachments/assets/88152234-1f9d-423c-a4df-243768ce5728" />

The box also has a lid, which will be attached and detached with magnets so the power bank used to power the Pi isn't perpeutally stuck in it. The hole on the side is to allow for the ports to stay exposed as needed.
