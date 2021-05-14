from flask import Flask
from flask import render_template,redirect,request
import sqlite3
from datetime import datetime


app=Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.route("/result/<theme>",methods=['POST','GET'])
def model1(theme):
    if(request.method=='POST'):
        params=dict()
        yourname=request.form["yourname"]
        profile_image=request.form["profile"]
        degree=request.form["degree"]
        about=request.form["about"]
        city=request.form["city"]
        email=request.form["email"]
        mobile=request.form["mobile"]
        params["yourname"]=yourname
        params["profile"]=profile_image
        params["degree"]=degree
        params["about"]=about
        params["city"]=city
        params["email"]=email
        params["mobile"]=mobile
        #Title
        title=request.form.getlist('title')
        params["title"]=title
        # Doing
        doing1=request.form["doing1"]
        doingDesc1=request.form["doingDesc1"]
        doing2=request.form["doing2"]
        doingDesc2=request.form["doingDesc2"]
        doing3=request.form["doing3"]
        doingDesc3=request.form["doingDesc3"]
        params["doingone"]=[doing1,doingDesc1]
        params["doingtwo"]=[doing2,doingDesc2]
        params["doingthree"]=[doing3,doingDesc3]
        #My Resume
        resume=degree1=request.form["resume"]
        params["resume"]=resume
        # Education Details
        degree1=request.form["degree1"]
        duration1=request.form["duration1"]
        collegeName1=request.form["collegeName1"]
        degree2=request.form["degree2"]
        duration2=request.form["duration2"]
        collegeName2=request.form["collegeName2"]
        degree3=request.form["degree3"]
        duration3=request.form["duration3"]
        collegeName3=request.form["collegeName3"]
        degree4=request.form["degree4"]
        duration4=request.form["duration4"]
        collegeName4=request.form["collegeName4"]
        params["degreeone"]=[degree1,duration1,collegeName1]
        params["degreetwo"]=[degree2,duration2,collegeName2]
        params["degreethree"]=[degree3,duration3,collegeName3]
        params["degreefour"]=[degree4,duration4,collegeName4]

        #Certification
        certi1=request.form["certi1"]
        credit1=request.form["credit1"]
        certi2=request.form["certi2"]
        credit2=request.form["credit2"]
        certi3=request.form["certi3"]
        credit3=request.form["credit3"]
        certi4=request.form["certi4"]
        credit4=request.form["credit4"]
        certi5=request.form["certi5"]
        credit5=request.form["credit5"]
        params["certificates"]=[[certi1,credit1],[certi2,credit2],[certi3,credit3],[certi4,credit4],[certi5,credit5]]
        jobTitle1=request.form["jobTitle1"]
        jobType1=request.form["jobType1"]
        jobCompany1=request.form["jobCompany1"]
        jobDuration1=request.form["jobDuration1"]
        jobDescription1=request.form["jobDescription1"]
        jobTitle2=request.form["jobTitle2"]
        jobType2=request.form["jobType2"]
        jobCompany2=request.form["jobCompany2"]
        jobDuration2=request.form["jobDuration2"]
        jobDescription2=request.form["jobDescription2"]
        jobTitle3=request.form["jobTitle3"]
        jobType3=request.form["jobType3"]
        jobCompany3=request.form["jobCompany3"]
        jobDuration3=request.form["jobDuration3"]
        jobDescription3=request.form["jobDescription3"]
        jobTitle4=request.form["jobTitle4"]
        jobType4=request.form["jobType4"]
        jobCompany4=request.form["jobCompany4"]
        jobDuration4=request.form["jobDuration4"]
        jobDescription4=request.form["jobDescription4"]
        jobTitle5=request.form["jobTitle5"]
        jobType5=request.form["jobType5"]
        jobCompany5=request.form["jobCompany5"]
        jobDuration5=request.form["jobDuration5"]
        jobDescription5=request.form["jobDescription5"]
        params["jobone"]=[jobTitle1,jobType1,jobCompany1,jobDuration1,jobDescription1]
        params["jobtwo"]=[jobTitle2,jobType2,jobCompany2,jobDuration2,jobDescription2]
        params["jobthree"]=[jobTitle3,jobType3,jobCompany3,jobDuration3,jobDescription3]
        params["jobfour"]=[jobTitle4,jobType4,jobCompany4,jobDuration4,jobDescription4]
        params["jobfive"]=[jobTitle5,jobType5,jobCompany5,jobDuration5,jobDescription5]

        #Project Details
        project1=request.form["project1"]
        project_u1=request.form["project_u1"]
        project_d1=request.form["project_d1"]
        project2=request.form["project2"]
        project_u2=request.form["project_u2"]
        project_d2=request.form["project_d2"]
        project3=request.form["project3"]
        project_u3=request.form["project_u3"]
        project_d3=request.form["project_d3"]
        project4=request.form["project4"]
        project_u4=request.form["project_u4"]
        project_d4=request.form["project_d4"]
        project5=request.form["project5"]
        project_u5=request.form["project_u5"]
        project_d5=request.form["project_d5"]
        project6=request.form["project6"]
        project_u6=request.form["project_u6"]
        project_d6=request.form["project_d6"]
        params["projectone"]=[project1,project_u1,project_d1]
        params["projecttwo"]=[project2,project_u2,project_d2]
        params["projectthree"]=[project3,project_u3,project_d3]
        params["projectfour"]=[project4,project_u4,project_d4]
        params["projectfive"]=[project5,project_u5,project_d5]
        params["projectsix"]=[project6,project_u6,project_d6]

        work_skill=request.form["work_skill"]
        achivements=request.form["achivements"]
        # Social Media

        touchMessage=request.form["touch_message"]
        github=request.form["github"]
        tw=request.form["twitter"]
        dev=request.form["dev"]
        codepen=request.form["codepen"]
        linkedin=request.form["linkedin"]
        stackoverflow=request.form["stackoverflow"]
        fb=request.form["fb"]
        instagram=request.form["instagram"]
        medium=request.form["medium"]
        youtube=request.form["youtube"]
        params["touch_message"]=touchMessage
        params["github"]=github
        params["twitter"]=tw
        params["dev"]=dev
        params["codepen"]=codepen
        params["linkedin"]=linkedin
        params["stackoverflow"]=stackoverflow
        params["fb"]=fb
        params["instagram"]=instagram
        params["medium"]=medium
        params["youtube"]=youtube
        work_skill=work_skill.split(",")
        achivements=achivements.split(",")
        params["work_skill"]=work_skill
        params["achivements"]=achivements

        return render_template("model/"+theme+"/"+theme+".html",params=params)


    else:
        return render_template("details.html")
@app.route("/details/<theme>")
def details(theme):
    return render_template("details.html",theme=theme)

@app.route("/demo/<theme>")
def demo(theme):
    return render_template("demo/"+theme+".html")

@app.route("/")
def ResumeBuilder():
    return render_template("ResumeBuilder.html")


if __name__=='__main__':
    app.run( debug=True)

