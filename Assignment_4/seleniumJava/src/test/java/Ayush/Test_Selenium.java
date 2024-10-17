package Ayush;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Test_Selenium {

    public static void main(String[] args) {
        // Set the ChromeDriver property
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\Ayush\\OneDrive\\Desktop\\Downloads\\chromedriver-win64\\chromedriver.exe");
        
        // Initialize WebDriver
        WebDriver driver = new ChromeDriver();

        // Navigate to Passport India website
        driver.navigate().to("https://www.passportindia.gov.in/");

        // Print the page title to check if navigation is successful
        System.out.println("Page Title: " + driver.getTitle());

        // Wait for 15 seconds
        try {
            Thread.sleep(15000); // Wait for 15 seconds (15000 milliseconds)
        } catch (InterruptedException e) {
            System.out.println("Sleep interrupted: " + e.getMessage());
        }
        
        // Close the browser
        driver.quit();
    }
}
