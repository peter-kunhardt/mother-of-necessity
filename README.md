# 📊 Pete's Data Portfolio
Welcome to my Portfolio! Here you can browse some sample projects, look at the underlying code, and execute a few limited commands to see the applications in action. Have fun poking around and drop me a line if you have comments, questions, or suggestions. 

## 🎆 How did this come about?
I wanted to create a portfolio of projects showcasing a breadth of analytics and data engineering projects: ETL services, dbt, Airflow, dashboarding, SQL, some little "fun" data widgets and so forth.

Unfortunately there are limited options for hosting that sort of portfolio. I could give you a link to a git, but to see most of it in action you'll have to clone the repo, install a bunch of stuff locally... let's face it you're not going to do that. I could put everything in a JupyterLabs project, but frankly I'm a notebook hater. (I think they encourage non-functional programming, don't @ me)

Enter this new project: a front end for your git repository that lets users navigate the repo, look at the code, and execute a few predefined statements which are configured in a config file you add to your repo so that users can see that your code executes and what it does.

## 🕰️ What's Next:

### 👷‍♂️ There are some things that don't work yet/are partially implemented:
- I need to define the structure of the config file. It should contain tags, the execution statements the app is allowed to execute... anything else?
- Category buttons at the top don't currently filter to relevant projects. (Need to create config file before that will work)
- Should probably pull the About and Contact information from the repo instead of saving server-side

### ▶️ Run Command Types:
- View documentation .md files **[Implemented]**
- Execute a python script and view its terminal output **[Implemented]**
- Launch and view a Streamlit or Metabase dashboard in a new window or modal. **[Partially Implemented with Streamlit - Not working]**
- Execute `dbt run -m _______` commands and receive tabular data output **[Not Implemented]**
- View dbt lineage chart **[Not Implemented]**
- Run (predefined) SQL against a demo Postgres and Iceberg instance **[Not Implemented]**
- Monitor a data streaming solution **[Not Implemented]**

### 🤝 Contributing:
- Feel free to raise an issue via the link at the top of this page, or drop me a line if you're interested in creating a portfolio of your own or helping develop the larger project.

## 📜 License & Use:
I've applied the MIT license here, feel free to clone the repo and launch your own in replit, just link folks back to this project!
