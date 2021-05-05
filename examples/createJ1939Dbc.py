#!/usr/bin/env python3
import canmatrix.formats

''' Initializing canmatrix as cm'''
cm = canmatrix.CANMatrix()

''' To create non-Extended CAN Message DBC '''
# messageIdentifier=canmatrix.ArbitrationId(id=0xDE,extended=False)
# CANMessageFrame = canmatrix.Frame("MessageName",arbitration_id=messageIdentifier)


''' To create Extended CAN Message DBC'''
# messageIdentifier=canmatrix.ArbitrationId(id=0x18ff013c,extended=True)
# CANMessageFrame = canmatrix.Frame("MessageName",arbitration_id=messageIdentifier)


''' To create J1939 complaint CAN Message DBC'''
CANMessageFrame = canmatrix.Frame("MessageName",is_j1939=True)
CANMessageFrame.pgn = 0xff01
CANMessageFrame.cycle_time = 1000
CANMessageFrame.source = 0x01
CANMessageFrame.priority = 0x03

''' To Create CAN signal

value table for a signal is described as dictionary example: {0: "off" ,1:"on", 2:"error",3: "reserved"}

Muxed messages can be input as multiplex="Multiplexor"(for the mux selector signal) and multiplex=1,2,3...n mux number.

'''
CANSignal= canmatrix.Signal("EngineTemperature", size=8, is_float=False,is_signed=False,factor=0.1,offset=-40, is_little_endian=True, start_bit=0,values={0:"Value Description 0",1:"Value Description 1"},comment="This is a comment",multiplex="1")


''' Adding a the above defined signal definition to the CAN message frame'''
CANMessageFrame.add_signal(CANSignal)
cm.add_frame(CANMessageFrame)
cm.recalc_dlc('force') # calculating the message dlc based on signal position

''' Saving the DBC in the project directory as "ExampleJ1939.dbc" '''
canmatrix.formats.dumpp({"":cm}, "ExampleJ1939.dbc")
