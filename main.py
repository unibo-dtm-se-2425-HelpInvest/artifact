
from flask import Flask, render_template, request, flash
import matplotlib.pyplot as plt
import numpy as np
import os as os

app = Flask(__name__)

@app.route("/", methods = ["GET"])  
def home():

    if request.method == "GET":
        if (request.args.get("years") == None):
            return render_template("homepage.html")
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
                    avgrate = 1.02
                    lowrate = 1.01
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
                    avgrate = 1.07
                    lowrate = 1.05
                    highrate = 1.09
                    
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
                    avgrate = 1.12
                    lowrate = 1.1
                    highrate = 1.14
                        
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
                
                
                
                plt.figure().set_figheight(6)
                plt.plot(timeline,highret, color = "green", label=f"High return at {int((highrate-1)*100)}%")
                plt.plot(timeline,avgret, color = "blue", label=f"Average return at {int((avgrate-1)*100)}%")
                plt.plot(timeline,lowret, color = "red", label=f"Low return at {int((lowrate-1)*100)}%")

                plt.ylim(bottom = capital)
                plt.legend()

            
                plt.xticks(np.arange(min(timeline), max(timeline)+1, (years/10)))
                plt.ticklabel_format(useOffset=False, style= "plain")

                plt.title(f"Projection for {years} years, with a capital of {capital}€")
                plt.xlabel("Years")
                plt.ylabel("Portfolio Value")

                plt.fill_between(timeline, highret, avgret, color = "green", alpha = 0.3)
                plt.fill_between(timeline, avgret, lowret, color = "blue", alpha = 0.3)
                plt.fill_between(timeline, lowret, color = "red", alpha = 0.3)


              

                script_dir = os.path.dirname(__file__ )
                results_dir = os.path.join(script_dir, 'static/images/')
                

                if not os.path.isdir(results_dir):
                    os.makedirs(results_dir)
                
                
                plt.savefig(results_dir + "plot.png", dpi = 300)
            
                
                return render_template("answer.html", capital = capital, years = years)










if __name__ == "__main__":
    app.run()
