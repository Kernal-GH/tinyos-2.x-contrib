#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'Msg'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 2

# The Active Message type associated with this message.
AM_TYPE = 204

class Msg(tinyos.message.Message.Message):
    # Create a new Msg of size 2.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=2):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <Msg> \n"
        try:
            s += "  [status=0x%x]\n" % (self.get_status())
        except:
            pass
        try:
            s += "  [ve_start_byte=0x%x]\n" % (self.get_ve_start_byte())
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: status
    #   Field type: short
    #   Offset (bits): 0
    #   Size (bits): 8
    #

    #
    # Return whether the field 'status' is signed (False).
    #
    def isSigned_status(self):
        return False
    
    #
    # Return whether the field 'status' is an array (False).
    #
    def isArray_status(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'status'
    #
    def offset_status(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'status'
    #
    def offsetBits_status(self):
        return 0
    
    #
    # Return the value (as a short) of the field 'status'
    #
    def get_status(self):
        return self.getUIntElement(self.offsetBits_status(), 8, 1)
    
    #
    # Set the value of the field 'status'
    #
    def set_status(self, value):
        self.setUIntElement(self.offsetBits_status(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'status'
    #
    def size_status(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'status'
    #
    def sizeBits_status(self):
        return 8
    
    #
    # Accessor methods for field: ve_start_byte
    #   Field type: byte
    #   Offset (bits): 8
    #   Size (bits): 8
    #

    #
    # Return whether the field 've_start_byte' is signed (False).
    #
    def isSigned_ve_start_byte(self):
        return False
    
    #
    # Return whether the field 've_start_byte' is an array (False).
    #
    def isArray_ve_start_byte(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 've_start_byte'
    #
    def offset_ve_start_byte(self):
        return (8 / 8)
    
    #
    # Return the offset (in bits) of the field 've_start_byte'
    #
    def offsetBits_ve_start_byte(self):
        return 8
    
    #
    # Return the value (as a byte) of the field 've_start_byte'
    #
    def get_ve_start_byte(self):
        return self.getSIntElement(self.offsetBits_ve_start_byte(), 8, 1)
    
    #
    # Set the value of the field 've_start_byte'
    #
    def set_ve_start_byte(self, value):
        self.setSIntElement(self.offsetBits_ve_start_byte(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 've_start_byte'
    #
    def size_ve_start_byte(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 've_start_byte'
    #
    def sizeBits_ve_start_byte(self):
        return 8
    