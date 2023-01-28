class Door:
    def __init__(self, length, width, height, color, shape, material, lock_combination):
        self.length = length
        self.width = width
        self.height = height
        self.color = color
        self.shape = shape
        self.material = material
        self.status = "closed"
        self.lock_status = "locked"
        self.lock_combination = lock_combination
        
    def unlock_door(self, lock_combination):
        if self.lock_status == "locked":
            if lock_combination == self.lock_combination:
                self.lock_status = "unlocked"
            else:
                print("Your lock combination is incorrect")
        else:
            print("Your door is already unlocked")
            
    def open_door(self, lock_combination):
        if self.lock_status == "unlocked":
            if self.status == "closed":
                self.status = "open"
            else:
                print("Your door's already open")
        else:
            unlock_door(self, lock_combination)
            self.status = "open"
         
    def close_door(self):
        if self.status == "open":
            self.status = "closed"
        else:
            print("Your door's already closed")
    
    def lock_door(self, lock_combination):
        if self.status == "open":
            close_door()
        if lock_combination == self.lock_combination:
            self.lock_status = "locked"
      
