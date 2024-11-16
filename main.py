#Base version of the project


from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import os as os

app = Flask(__name__)

@app.route("/", methods = ["GET"])  
def home():

    if request.method == "GET":
        if (request.args.get("years") == None):
            return render_template("HelpInvest.html")
        elif(request.args.get("years") == ""):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            years = request.args.get("years")
            if(request.args.get("capital") == ""):
                return "<html><body> <h1>Invalid number</h1></body></html>"
            else:            
                capital = request.args.get("capital")

                capital = int(capital)
                years = int(years)

                timeline = []
                avgret = []
                lowret = []
                highret = []
                year = 2024
                timeline.append(year)
                
                avgret.append(capital)
                lowret.append(capital)
                highret.append(capital)
                

                for i in range(years):
                    year += 1
                    timeline.append(year)
                    i += 1
                
                if request.args.get("risk_profile") == "low":
                    avgrate = 1.025
                    lowrate = 1.02
                    highrate = 1.03
                
                    i = 0
                    avgcapital = capital
                    for i in range(years):   
                        avgcapital = avgcapital*avgrate
                        i += 1
                        avgret.append(avgcapital)
                    
                    i= 0
                    lowcapital = capital
                    for i in range(years):
                        lowcapital = lowcapital*lowrate
                        i += 1
                        lowret.append(lowcapital)
                    
                    i = 0
                    highcapital = capital
                    for i in range(years):
                        highcapital = highcapital*highrate
                        i += 1
                        highret.append(highcapital)   

                if request.args.get("risk_profile") == "medium":
                    avgrate = 1.1
                    lowrate = 1.05
                    highrate = 1.15
                    
                    i = 0
                    avgcapital = capital
                    for i in range(years):   
                        avgcapital = avgcapital*avgrate
                        i += 1
                        avgret.append(avgcapital)
                    
                    i= 0
                    lowcapital = capital
                    for i in range(years):
                        lowcapital = lowcapital*lowrate
                        i += 1
                        lowret.append(lowcapital)
                    
                    i = 0
                    highcapital = capital
                    for i in range(years):
                        highcapital = highcapital*highrate
                        i += 1
                        highret.append(highcapital)
                    

                if request.args.get("risk_profile") == "high":
                    avgrate = 1.2
                    lowrate = 1.1
                    highrate = 1.3
                        
                    i = 0
                    avgcapital = capital
                    for i in range(years):   
                        avgcapital = avgcapital*avgrate
                        i += 1
                        avgret.append(avgcapital)
                        
                    i= 0
                    lowcapital = capital
                    for i in range(years):
                        lowcapital = lowcapital*lowrate
                        i += 1
                        lowret.append(lowcapital)
                        
                    i = 0
                    highcapital = capital
                    for i in range(years):
                        highcapital = highcapital*highrate
                        i += 1
                        highret.append(highcapital)


                timeline = np.array(timeline)
                avgret = np.array(avgret)
                lowret = np.array(lowret)
                highret = np.array(highret)

                plt.plot(timeline,avgret, color = "b")
                plt.plot(timeline,highret, color = "g")
                plt.plot(timeline,lowret, color = "r")
                

                script_dir = os.path.dirname(__file__ )
                results_dir = os.path.join(script_dir, 'static/images/')
                

                if not os.path.isdir(results_dir):
                    os.makedirs(results_dir)
                
                
                plt.savefig(results_dir + "plot.png")
            
                
                return render_template("answer.html", capital = capital, years = years)










if __name__ == "__main__":
    app.run()
