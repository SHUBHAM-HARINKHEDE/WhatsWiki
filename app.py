from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/whatsapp", methods=["POST"])
def reply_whatsapp():
    #fetch msg
    msg = request.form.get("Body")
    #create reply
    response = MessagingResponse()
    page_py = wiki_wiki.page(msg)  #get data from wikipedia
    res="No result found for:'"+msg+"'"
    if page_py.exists():
        res=str(page_py.title)+"\n"+str(page_py.summary[0:500])+"...\nfor more visit:"+str(page_py.fullurl)
    #send reply
    response.message(res)
    return str(response)

if __name__ == "__main__":
    app.run()
