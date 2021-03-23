# MAVLink CRC

MAVLink code that needs to use a Cyclic Redundancy Check (CRC) should choose the CRC32 implementation described below.

> **Note** Using the same CRC implementation for all cases means that only one implementation is required. 
  Do not introduce another unless there without a compelling technical reason.


## CRC32 Implementation

The CRC32 algorithm used by MAVLink is similar to (but different from) the ISO 3309 standard based on the polygon 0x04C11DB7.
It is commonly referred to as "the CRC32 based on Gary Brown's work".

The difference of MAVLink's implementation versus the standard are:
- Start at 0 instead of `0xFFFFFFFF`.
- Missing final XOR out operation with `0xFFFFFFFF`.

The effects of the initial value and final XOR operation are documented in this [brief tutorial on CRC computation of the Linux kernel](https://github.com/torvalds/linux/blob/master/Documentation/staging/crc32.rst).

This implementation is currently used in:
- [File Transfer Protocol (FTP)](../services/ftp.md)
* [Parameter Protocol > PX4 Implementation](../services/parameter.md#px4) (Implementation-specific hash of cached parameters).
