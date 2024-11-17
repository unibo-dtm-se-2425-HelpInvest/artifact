
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import os as os

app = Flask(__name__)

@app.route("/", methods = ["GET"])  
def home():

    if request.method == "GET":
       
        if (request.args.get("years") == None):
            return render_template("homepage.html")
        
        elif(request.args.get("years") != ""):
                       
            capital = request.args.get("capital")
            years = request.args.get("years")
            monthly_deposit = request.args.get("monthly_deposit")

            monthly_deposit = int(monthly_deposit)
            yearly_deposit = monthly_deposit * 12    
            capital = int(capital)
            years = int(years)

            timeline = []
            avgret = []
            lowret = []
            highret = []
            noret = []
            year = 2024
            timeline.append(year)
            
            avgret.append(capital)
            lowret.append(capital)
            highret.append(capital)
            noret.append(capital)
            

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
                    avgcapital = (avgcapital+yearly_deposit)*avgrate
                    i += 1
                    avgret.append(avgcapital)
                
                i= 0
                lowcapital = capital
                for i in range(years):
                    lowcapital = (lowcapital+yearly_deposit)*lowrate
                    i += 1
                    lowret.append(lowcapital)
                
                i = 0
                highcapital = capital
                for i in range(years):
                    highcapital = (highcapital+yearly_deposit)*highrate
                    i += 1
                    highret.append(highcapital)   

            if request.args.get("risk_profile") == "medium":
                avgrate = 1.07
                lowrate = 1.05
                highrate = 1.09
                
                i = 0
                avgcapital = capital
                for i in range(years):   
                    avgcapital = (avgcapital+yearly_deposit)*avgrate
                    i += 1
                    avgret.append(avgcapital)
                
                i= 0
                lowcapital = capital
                for i in range(years):
                    lowcapital = (lowcapital+yearly_deposit)*lowrate
                    i += 1
                    lowret.append(lowcapital)
                
                i = 0
                highcapital = capital
                for i in range(years):
                    highcapital = (highcapital+yearly_deposit)*highrate
                    i += 1
                    highret.append(highcapital)
                

            if request.args.get("risk_profile") == "high":
                avgrate = 1.12
                lowrate = 1.1
                highrate = 1.14
                    
                i = 0
                avgcapital = capital
                for i in range(years):   
                    avgcapital = (avgcapital+yearly_deposit)*avgrate
                    i += 1
                    avgret.append(avgcapital)
                    
                i= 0
                lowcapital = capital
                for i in range(years):
                    lowcapital = (lowcapital+yearly_deposit)*lowrate
                    i += 1
                    lowret.append(lowcapital)
                    
                i = 0
                highcapital = capital
                for i in range(years):
                    highcapital = (highcapital+yearly_deposit)*highrate
                    i += 1
                    highret.append(highcapital)
            
            i = 0
            nocapital = capital
            for i in range(years):
                nocapital += yearly_deposit
                i += 1
                noret.append(nocapital)
            


            timeline = np.array(timeline)
            avgret = np.array(avgret)
            lowret = np.array(lowret)
            highret = np.array(highret)
            noret = np.array(noret)
            
            
            plt.figure().set_figwidth(6)
            plt.figure().set_figheight(6)
            plt.plot(timeline,highret, color = "green", label=f"High return at {int((highrate-1)*100)}%")
            plt.plot(timeline,avgret, color = "blue", label=f"Average return at {int((avgrate-1)*100)}%")
            plt.plot(timeline,lowret, color = "red", label=f"Low return at {int((lowrate-1)*100)}%")
            plt.plot(timeline,noret, color = "grey", label = f"Base capital with no return")
            plt.legend()

        
            plt.xticks(np.arange(min(timeline), max(timeline)+1, (years/10)))
            plt.ticklabel_format(useOffset=False, style= "plain")

            plt.title(f"{years} years, base capital of {capital}€ and monthly deposits of {monthly_deposit}€")
            plt.xlabel("Years")
            plt.ylabel("Portfolio Value")

            plt.fill_between(timeline, highret, avgret, color = "green", alpha = 0.3)
            plt.fill_between(timeline, avgret, lowret, color = "blue", alpha = 0.3)
            plt.fill_between(timeline, lowret, noret,color = "red", alpha = 0.3)
            plt.fill_between(timeline, noret, color = "grey", alpha = 0.3)

            
            

            script_dir = os.path.dirname(__file__ )
            results_dir = os.path.join(script_dir, 'static/images/')
            

            if not os.path.isdir(results_dir):
                os.makedirs(results_dir)
            
            
            plt.savefig(results_dir + "plot.png", bbox_inches = "tight", pad_inches = 0.2,dpi = 300)
        
            
            return render_template("second_page.html", capital = capital, years = years)










if __name__ == "__main__":
    app.run()
