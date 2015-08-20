from NTSTATUS import *;

dsId_uCode = {
  STATUS_WX86_SINGLE_STEP: "WoW64SingleStep",
  STATUS_WX86_BREAKPOINT: "WoW64Breakpoint",
  0x40080201: "WRTOriginate",
  0x406D1388: "ThreadName",
  STATUS_GUARD_PAGE_VIOLATION: "GuardPage",
  STATUS_DATATYPE_MISALIGNMENT: "DataMisalign",
  STATUS_BREAKPOINT: "Breakpoint",
  STATUS_SINGLE_STEP: "SingleStep",
  0x8007000E: "OOM",
  STATUS_ACCESS_VIOLATION: "AV", # Special cased if exception parameters are available
  STATUS_IN_PAGE_ERROR: "InPageIO",
  STATUS_INVALID_HANDLE: "InvalidHandle",
  STATUS_NO_MEMORY: "OOM",
  STATUS_ILLEGAL_INSTRUCTION: "IllegalInstr",
  STATUS_NONCONTINUABLE_EXCEPTION: "NonContinuable",
  STATUS_INVALID_DISPOSITION: "InvalidDisposition",
  STATUS_ARRAY_BOUNDS_EXCEEDED: "ArrayBounds",
  STATUS_FLOAT_DENORMAL_OPERAND: "FloatDenormalOperand",
  STATUS_FLOAT_DIVIDE_BY_ZERO: "FloatDiv0",
  STATUS_FLOAT_INEXACT_RESULT: "FloatInexactResult",
  STATUS_FLOAT_INVALID_OPERATION: "FloatInvalidOperation",
  STATUS_FLOAT_OVERFLOW: "FloatOverflow",
  STATUS_FLOAT_STACK_CHECK: "FloatStackCheck",
  STATUS_FLOAT_UNDERFLOW: "FloatUnderflow",
  STATUS_INTEGER_DIVIDE_BY_ZERO: "IntDiv0",
  STATUS_INTEGER_OVERFLOW: "IntOverflow",
  STATUS_PRIVILEGED_INSTRUCTION: "PrivInstr",
  STATUS_STACK_OVERFLOW: "StackExhaust",
  0xC000027B: "WRTLanguage",
  STATUS_STACK_BUFFER_OVERRUN: "FF", # Special cased if exception parameters are available
  0xC000041D: "Verifier",
  STATUS_FAIL_FAST_EXCEPTION: "FailFast",
  0xE06D7363: "C++",
};
def fsGetExceptionTypeId(uCode):
  return dsId_uCode.get(uCode) or "0x%08X" % uCode;