mul  = "f30fb845cc83e00185c074398b45ccc1e80989c2488b45f84801d00fb6008b55cc4889d183e10f488b55f84801ca0fb60a8b55ccc1ea0989d6488b55f84801f20fafc18802488b45e0bf00000000ffd0488d05a9ffffff488945d89090488b45d8488b55e8be010000004889c7ffd290c9c3"
eq   = "f30fb845cc83e00185c0743b8b45ccc1e80989c2488b45f84801d00fb6108b45cc83e00f4889c1488b45f84801c80fb60038c20f94c28b45ccc1e80989c1488b45f84801c88810488b45e0bf00000000ffd0488d05a7ffffff488945d8488b45d8488b55e8be020000004889c7ffd290c9c3"
add1 = "f30fb845cc83e00185c074388b45ccc1e80989c2488b45f84801d00fb6088b45cc83e00f4889c2488b45f84801d00fb6108b45ccc1e80989c6488b45f84801f001ca8810488b45e0bf00000000ffd0909090488d05a7ffffff488945d8488b45d8488b55e8be030000004889c7ffd290c9c3"
mov1 = "f30fb845cc83e00185c074318b45cc83e00f4889c2488b45f84801d08b55ccc1ea0989d1488b55f84801ca0fb6120fb6ca488b55f04801ca0fb6008802488b45e0bf00000000ffd090909090909090909090488d05a7ffffff488945d8488b45d8488b55e8be040000004889c7ffd290c9c3"
mov2 = "f30fb845cc83e00185c074318b45cc83e00f4889c2488b45f84801d00fb6000fb6d0488b45f04801d08b55ccc1ea0989d1488b55f84801ca0fb6008802488b45e0bf00000000ffd090909090909090909090488d05a7ffffff488945d8488b45d8488b55e8be050000004889c7ffd290c9c3"
mod  = "f30fb845cc83e00185c074338b45ccc1e80989c2488b45f84801d00fb6000fb6c08b55cc0fb6caba00000000f7f18b45ccc1e80989c1488b45f84801c88810488b45e0bf00000000ffd09090909090909090488d05a7ffffff488945d8488b45d8488b55e8be060000004889c7ffd290c9c3"
out  = "f30fb845cc83e00185c0742a8b45ccc1e80989c2488b45f84801d00fb6000fb6d0488b45f04801d00fb6000fb6c0488b55e089c7ffd290909090909090909090909090909090909090909090909090909090488d05a7ffffff488945d8488b45d8488b55e8be070000004889c7ffd290c9c3"
add0 = "f30fb845cc83e00185c0742a8b45ccc1e80989c2488b45f84801d00fb6108b45cc89c18b45ccc1e80989c6488b45f84801f001ca8810488b45e0bf00000000ffd09090909090909090909090909090909090488d05a7ffffff488945d8488b45d8488b55e8be080000004889c7ffd290c9c3"
inp  = "f30fb845cc83e00185c0742b488b45e0bfffffffffffd089c28b45ccc1e80989c1488b45f84801c80fb6000fb6c8488b45f04801c88810909090909090909090909090909090909090909090909090909090488d05a7ffffff488945d8488b45d8488b55e8be090000004889c7ffd290c9c3"
mov0 = "f30fb845cc83e00185c074148b45ccc1e80989c2488b45f84801d08b55cc8810488b45e0bf00000000ffd0909090909090909090909090909090909090909090909090909090909090909090909090909090488d05a7ffffff488945d8488b45d8488b55e8be0a0000004889c7ffd290c9c3"

fml = 0
for i in range(0, len(eq), 2):
    x1 = int(mov0[i:i+2], 16)
    x2 = int(mul[i:i+2], 16)
    x = x1^x2
    print("\\x" + hex(x)[2:], end="")
    fml += 1
print()
print(fml)