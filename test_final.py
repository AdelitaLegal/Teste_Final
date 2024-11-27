#python -m pytest test_final
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestDemo:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://tdd-detroid.onrender.com/")
        self.driver.set_window_size(970, 555)

        # Aguarde até que a sobreposição desapareça
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.ID, "pyscript_loading_splash"))
        )

        self.driver.find_element(By.ID, "student-nome").click()
        self.driver.find_element(By.ID, "student-nome").send_keys("douglas")
        self.driver.find_element(By.ID, "student-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-p").click()
        assert "INFO Added student id: 1, Name: douglas" in self.driver.find_element(By.CSS_SELECTOR, ".py-p").text

        self.driver.find_element(By.ID, "course-nome").click()
        self.driver.find_element(By.ID, "course-nome").send_keys("mat")
        self.driver.find_element(By.ID, "course-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(2)").click()
        assert "INFO Added student id: 1, Name: douglas" in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(2)").text

        self.driver.find_element(By.ID, "student-id").click()
        self.driver.find_element(By.ID, "student-id").send_keys("1")
        self.driver.find_element(By.ID, "course-id").click()
        self.driver.find_element(By.ID, "course-id").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(3)").click()
        assert "INFO Added student id: 1, Name: douglas" in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(3)").text

        self.driver.find_element(By.ID, "discipline-nome").click()
        self.driver.find_element(By.ID, "discipline-nome").send_keys("mat")
        self.driver.find_element(By.ID, "course-discipline-id").click()
        self.driver.find_element(By.ID, "course-discipline-id").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").click()
        assert "FAIL Necessários 3 cursos para se criar a primeira matéria" in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text

        self.driver.find_element(By.ID, "course-nome").click()
        self.driver.find_element(By.ID, "course-nome").send_keys("port")
        self.driver.find_element(By.ID, "course-btn").click()
        self.driver.find_element(By.ID, "course-nome").click()
        self.driver.find_element(By.ID, "course-nome").send_keys("geo")
        self.driver.find_element(By.ID, "course-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").click()
        assert "INFO Added discipline id: 1, Name: mat, Course: 1" in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text

        self.driver.find_element(By.ID, "discipline-nome").click()
        self.driver.find_element(By.ID, "discipline-nome").send_keys("mat2")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()
        self.driver.find_element(By.ID, "discipline-nome").click()
        self.driver.find_element(By.ID, "discipline-nome").send_keys("mat3")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()
        self.driver.find_element(By.ID, "subscribe-student-id").click()
        self.driver.find_element(By.ID, "subscribe-student-id").send_keys("1")
        self.driver.find_element(By.ID, "subscribe-discipline-id").click()
        self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").click()
        assert "WARN Aluno deve se inscrever em 3 materias no minimo" in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text

        self.driver.find_element(By.ID, "subscribe-discipline-id").click()
        self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys("2")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()
        self.driver.find_element(By.ID, "subscribe-discipline-id").click()
        self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()
        self.driver.find_element(By.ID, "discipline-nome").click()
        self.driver.find_element(By.ID, "discipline-nome").send_keys("mat4")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()
        self.driver.find_element(By.ID, "subscribe-discipline-id").click()
        self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()
        self.driver.close()
