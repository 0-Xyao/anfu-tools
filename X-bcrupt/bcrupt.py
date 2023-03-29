import os
import logging
import concurrent.futures
import time
import bcrypt
from bcrypt import checkpw



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LowPasswordChecker:
    def __init__(self):
        self.folder = "/Users/你的用户名/IdeaProjects/lower-password-check/src/main/resources"
        self.log = logging.getLogger(self.__class__.__name__)
        self.totalSize = 0
        self.counter = 0
        self.matchesPasswordPath = os.path.join(self.folder, "matches-password.txt")
        
        self.lowPasswords = []
        with open(os.path.join(self.folder, "password.txt"), "r") as f:
            self.lowPasswords = f.read().splitlines()
        self.hashedList = []
        with open(os.path.join(self.folder, "bcrypt.txt"), "r") as f:
            self.hashedList = f.read().splitlines()
        
        self.totalSize = len(self.hashedList) * len(self.lowPasswords)
        
    def execute(self):
        with open(self.matchesPasswordPath, "a") as f:
            with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
                for lowPasswordsPartList in self.chunk_list(self.lowPasswords, 10):
                    for hashedPasswordPartList in self.chunk_list(self.hashedList, 10):
                        for lowPassword in lowPasswordsPartList:
                            for hashedPassword in hashedPasswordPartList:
                                if checkpw(lowPassword.encode(), hashedPassword.encode()):
                                    f.write(f"{lowPassword}:{hashedPassword}\n")
                                    f.flush()
                                    self.log.info("密码匹配成功：弱密码 【 %s 】 加密后密码 【 %s 】", lowPassword, hashedPassword)
                                self.counter += 1
        self.log.info("{}/{} 进度 {}%", self.counter, self.totalSize, (self.counter/self.totalSize)*100)
    
    def chunk_list(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

if __name__ == "__main__":
    checker = LowPasswordChecker()
    checker.execute()
