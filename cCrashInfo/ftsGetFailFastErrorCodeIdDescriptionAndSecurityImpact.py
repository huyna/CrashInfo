# Source: winnt.h (codemachine.com/downloads/win81/winnt.h)
dsFailFastErrorCodes = {                                          # I have not checked if the below is true, plz confirm.
  0:  ("LegacyGS",      "FAST_FAIL_LEGACY_GS_VIOLATION",          "Potentially exploitable security issue"),
  1:  ("VTGuard",       "FAST_FAIL_VTGUARD_CHECK_FAILURE",        "Potentially exploitable security issue"),
  2:  ("StackCookie",   "FAST_FAIL_STACK_COOKIE_CHECK_FAILURE",   "Potentially exploitable security issue"),
  3:  ("CorruptList",   "FAST_FAIL_CORRUPT_LIST_ENTRY",           "Potentially exploitable security issue"),
  4:  ("BadStack",      "FAST_FAIL_INCORRECT_STACK",              "Potentially exploitable security issue"),
  5:  ("InvalidArg",    "FAST_FAIL_INVALID_ARG",                  "Potentially exploitable security issue"),
  6:  ("GSCookie",      "FAST_FAIL_GS_COOKIE_INIT",               "Potentially exploitable security issue"),
  7:  ("AppExit",       "FAST_FAIL_FATAL_APP_EXIT",               "Potentially exploitable security issue"),
  8:  ("RangeCheck",    "FAST_FAIL_RANGE_CHECK_FAILURE",          "Potentially exploitable security issue"),
  9:  ("Registry",      "FAST_FAIL_UNSAFE_REGISTRY_ACCESS",       "Potentially exploitable security issue"),
  10: ("GuardICall",    "FAST_FAIL_GUARD_ICALL_CHECK_FAILURE",    "Potentially exploitable security issue"),
  11: ("GuardWrite",    "FAST_FAIL_GUARD_WRITE_CHECK_FAILURE",    "Potentially exploitable security issue"),
  12: ("FiberSwitch",   "FAST_FAIL_INVALID_FIBER_SWITCH",         "Potentially exploitable security issue"),
  13: ("SetContext",    "FAST_FAIL_INVALID_SET_OF_CONTEXT",       "Potentially exploitable security issue"),
  14: ("RefCount",      "FAST_FAIL_INVALID_REFERENCE_COUNT",      "Potentially exploitable security issue"),
  18: ("JumpBuffer",    "FAST_FAIL_INVALID_JUMP_BUFFER",          "Potentially exploitable security issue"),
  19: ("MrData",        "FAST_FAIL_MRDATA_MODIFIED",              "Potentially exploitable security issue"),
  20: ("Cert",          "FAST_FAIL_CERTIFICATION_FAILURE",        "Potentially exploitable security issue"),
  21: ("ExceptChain",   "FAST_FAIL_INVALID_EXCEPTION_CHAIN",      "Potentially exploitable security issue"),
  22: ("Crypto",        "FAST_FAIL_CRYPTO_LIBRARY",               "Potentially exploitable security issue"),
  23: ("DllCallout",    "FAST_FAIL_INVALID_CALL_IN_DLL_CALLOUT"   "Potentially exploitable security issue"),
  24: ("ImageBase",     "FAST_FAIL_INVALID_IMAGE_BASE",           "Potentially exploitable security issue"),
  25: ("DLoadProt",     "FAST_FAIL_DLOAD_PROTECTION_FAILURE",     "Potentially exploitable security issue"),
  26: ("ExtCall",       "FAST_FAIL_UNSAFE_EXTENSION_CALL",        "Potentially exploitable security issue"),
};

def ftsGetFailFastErrorCodeIdDescriptionAndSecurityImpact(uCode):
  return dsFailFastErrorCodes.get(uCode, ("Unknown", "unknown fail fast code", "May be a security issue"));