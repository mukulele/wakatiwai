{
  'variables': {
    'rest_max_chunk_size': '16384',
    'base64_dir': '<(deps_dir)/base64',
    'tinydtls_dir': '<(deps_dir)/tinydtls',
    'wakaama_dtls_dir':
    '<(deps_dir)/wakaama/examples/shared/tinydtls',
    'wakaama_dtls_sources': [
      '<(wakaama_dtls_dir)/ccm.c',
      '<(wakaama_dtls_dir)/crypto.c',
      '<(wakaama_dtls_dir)/dtls_debug.c',
      '<(wakaama_dtls_dir)/dtls_time.c',
      '<(wakaama_dtls_dir)/dtls.c',
      '<(wakaama_dtls_dir)/hmac.c',
      '<(wakaama_dtls_dir)/netq.c',
      '<(wakaama_dtls_dir)/peer.c',
      '<(wakaama_dtls_dir)/session.c',
      '<(wakaama_dtls_dir)/sha2/sha2.c',
      '<(wakaama_dtls_dir)/aes/rijndael.c',
      '<(wakaama_dtls_dir)/ecc/ecc.c',
    ],
  'wakaama_core_dir': '<(deps_dir)/wakaama/core',
    'wakaama_core_sources': [
      '<(deps_dir)/wakaama/coap/er-coap-13/er-coap-13.c',
      '<(wakaama_core_dir)/bootstrap.c',
      # Use modern data layer from deps/wakaama/data
      '<(deps_dir)/wakaama/data/data.c',
      '<(wakaama_core_dir)/discover.c',
      '<(wakaama_core_dir)/liblwm2m.c',
      '<(wakaama_core_dir)/list.c',
      '<(wakaama_core_dir)/management.c',
      '<(wakaama_core_dir)/objects.c',
      '<(wakaama_core_dir)/observe.c',
      '<(wakaama_core_dir)/registration.c',
      '<(wakaama_core_dir)/packet.c',
      # Use coap/transaction.c implementation (provides transaction_set_payload and transaction_free_userData)
      '<(deps_dir)/wakaama/coap/transaction.c',
      '<(wakaama_core_dir)/uri.c',
      '<(wakaama_core_dir)/utils.c',
    ],
    'wakaama_example_dir': '<(deps_dir)/wakaama/examples',
    'wakaama_client_dir': '<(wakaama_example_dir)/client',
    'wakaama_shared_dir': '<(wakaama_example_dir)/shared',
    'wakaama_client_shared_sources': [],
    'wakaama_server_shared_sources': [],
    'wakaama_server_dir': '<(wakaama_example_dir)/server',
    'wakaama_server_sources': [],
    'wakaama_bootstrap_server_dir': '<(wakaama_example_dir)/bootstrap_server',
    'wakaama_bootstrap_server_sources': [],
    'wakaama_defines': [
      'LWM2M_LITTLE_ENDIAN=<!(python <(deps_dir)/endianess.py)',
      'REST_MAX_CHUNK_SIZE=<(rest_max_chunk_size)',
      'LWM2M_COAP_DEFAULT_MAX_RETRANSMIT=4',
      'LWM2M_COAP_SEPARATE_TIMEOUT=5',
    ],
    'wakaama_client_defines': [
      '<@(wakaama_defines)',
      'LWM2M_BOOTSTRAP',
      'LWM2M_CLIENT_MODE',
      'LWM2M_SUPPORT_TLV',
      'WITH_TINYDTLS',
      'DTLSv12',
      'WITH_SHA256',
      'DTLS_PSK',
      'DTLS_ECC',
    ],
    'wakaama_sever_defines': [
      '<@(wakaama_defines)',
      'LWM2M_BOOTSTRAP',
      'LWM2M_SERVER_MODE',
    ],
    'wakaama_bootstrap_sever_defines': [
      '<@(wakaama_defines)',
      'LWM2M_BOOTSTRAP_SERVER_MODE',
    ],
  },
  'target_defaults': {
    'default_configuration': 'Release',
    'configurations': {
      'Debug': {
        'defines': [
          'LWM2M_WITH_LOGS',
          'WITH_LOGS',
        ],
        'defines!': [
          'NDEBUG',
        ],
        'cflags_cc!': [
          '-O3',
          '-Os',
        ],
        'cflags_cc': [
          '-std=c++11',
        ],
        'xcode_settings': {
          'MACOSX_DEPLOYMENT_TARGET': '10.7',
          'OTHER_CPLUSPLUSFLAGS!': [
            '-O3',
            '-Os',
            '-DDEBUG'
          ],
          'OTHER_CPLUSPLUSFLAGS': [
            '-std=c++11',
            '-stdlib=libc++',
          ],
          'GCC_OPTIMIZATION_LEVEL': '0',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES',
          'GCC_ENABLE_CPP_RTTI': 'YES',
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          'MACOSX_DEPLOYMENT_TARGET': '10.9',
          'CLANG_CXX_LIBRARY': 'libc++',
          'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
          'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
        },
      },
      'Release': {
        'defines': [
          'NDEBUG',
        ],
        'defines!': [
          'LWM2M_WITH_LOGS',
          'WITH_LOGS',
        ],
        'cflags_cc!': [
          '-DLWM2M_WITH_LOGS',
          '-DWITH_LOGS',
        ],
        'cflags_cc': [
          '-std=c++11',
        ],
        'xcode_settings': {
          'OTHER_CPLUSPLUSFLAGS!': [
            '-Os',
            '-O2'
          ],
          'OTHER_CPLUSPLUSFLAGS': [
            '-std=c++11',
            '-stdlib=libc++',
          ],
          'GCC_OPTIMIZATION_LEVEL': '3',
          'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
          'GCC_ENABLE_CPP_RTTI': 'YES',
          'DEAD_CODE_STRIPPING': 'YES',
          'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES',
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          'MACOSX_DEPLOYMENT_TARGET': '10.9',
          'CLANG_CXX_LIBRARY': 'libc++',
          'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
          'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
        },
      }
    }
  }
}
