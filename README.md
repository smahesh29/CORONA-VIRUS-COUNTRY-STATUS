# CORONA-VIRUS-COUNTRY-STATUS

<h2>Objective :</h2>
<p>To get corona virus real-time count of a country through Email.</p>

<h2>About the Project :</h2>
<p>In this Python Project, I had scraped data form https://www.worldometers.info/coronavirus/ using selenium and send data of requested country through Mail.</p>

<h2>Installation and Configuration :</h2>
<ol>
  <li><h4>Download ChromeDriver</h4></li> 
  <p>Download ChromeDriver according to your Chrome Version and OS form <a href = "https://chromedriver.chromium.org/downloads">here</a> and place it in ChromeDriver folder. The current ChromeDriver is for Chrome version 80 and for Windows System.</p>
  <li><h4>Install Required Libraries</h4></li>
  
      pip install -r requirements.txt
      
  <li><h4>Configuration</h4></li>
  <ul>
    <li>Open config.json file</li>
    <li>Write your email address at line 5 in place of <b>your_email_address</b></li>
    <li>Write App passward at line 6 in place of <b>App Passwords</b> Refer <a href = "https://support.google.com/accounts/answer/185833">this</a> for Creating App passward</li>
  </ul>
 </ol>
  
   <h2>Usage :</h2>
   <p>Use Command :</p>
    
      python main.py
      
