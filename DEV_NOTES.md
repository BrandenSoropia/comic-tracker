# What is this?

A place to leave thoughts, discoveries, struggles and everything else!

## Dec 27, 2020

I want to try a refresh myself and enjoy programming again. I've been doing frontend with React and JS for a while and I think changing it up and trying something completely new will fun/reinvigorating!

I chose Python because Figure 1 (current workplace) uses it. It helps that it's pretty simple syntactically and I'm slightly familiar with it from the school days. Also I discovered it comes with sqlite (according to Flask docs, it's good for small projects) so that helps with setting things up!

However, I'm new to venv and package manager pip, The ideas are simple but I'm not going to touch them unless I have to! Also my OOP/Python game is weak, so that's going to have to level up too!

## Dev 29, 2020
venv is great. It's really nice to run my app in its own little world, and if the future, make it easier to switch between other Python projects. I just need to remember to run the app in a virtual environment first!

## Dec 31, 2020
Sending emails:

(For testing/sending eamils locally) It seems pretty simple actually! Python seems amazing and comes with everything out of the box.

MailTrap:
Finding MailTrap was awesome. It makes this whole process so much easier, spits out super basic starter code in various languages and actually seeing the sent email is really nice!

I wanted to try `smtpd`, but I ran into out-dated tutorials/lost patience with docs and couldn't get it to work sadly. It would be nice to use it since it comes with Python right out of the box and is 100% free (with the added expense of having to manually render the email HTML in browser).

Now the next step:
Designing emails. I want to see how to include styles. I heard this was the painful part, I guess I'll find out haha. Also I need to see if there's an easier way to populate emails with data. I remember seeing a Go email template library at League, where it provided an API to pass in data into an HTML template more flexibly than the basic `smtplib`/`MIMEMultipart` way.

A note about images in emails:
Apparently if you just drop an image into an email as a CID attachment (embedded as a MIME object, not sure what either of those mean fully), popular email providers are more likely to mark it as spam! CID's show up as both HTML and an attachment

The way to show an image, but without attachment, is via base64 images (inline embedding). Pretty much does some magic to encode an image file, and puts that encoding into the HTML, which then magically decodes it into an image. Let me say this about all that, it's M A G I C.`