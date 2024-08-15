class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        def update_register(register, remainder):
            ini_len = len(register)

            if remainder in [10,15]:
                try: register.remove(10)
                except: pass
                else: remainder -= 10

            while remainder > 0:
                try: register.remove(5)
                except: break
                else: remainder -= 5

            return register, remainder, ini_len - len(register)


        i = 0
        while i < len(bills):
            if bills[i] == 5:
                i += 1
            elif i == 0:
                return False
            else:
                remainder = bills[i] - 5
                register, remainder, removed = update_register(bills[:i], remainder)
                if remainder != 0:
                    return False
                else:
                    bills = register + bills[i:]
                    i = i - removed + 1
        return True
