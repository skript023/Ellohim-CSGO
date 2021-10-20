from pattern_scanner import pm

class Memory():
    def get_pointer(self, Address, offsets : list[int] = ()) -> int:
        temp_addr = pm.read_int(Address)
        ptr = 0x0
        if not offsets: return Address
        else:
            for offset in offsets:
                ptr = int(str(temp_addr), 0) + int(str(offset), 0)
                temp_addr = pm.read_int(ptr)
            return ptr