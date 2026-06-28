# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from .modules import (
    Embedding,
    Embedding4bit,
    Embedding8bit,
    EmbeddingFP4,
    EmbeddingNF4,
    Int8Params,
    Linear4bit,
    Linear8bitLt,
    LinearFP4,
    LinearNF4,
    LinearNF4Compute,
    LinearApproxFP32,
    LinearApproxFP16,
    LinearApproxFP8E4M3,
    LinearApproxFP8E5M2,
    LinearApproxBfloat16,
    LinearApproxMitchell,
    LinearApproxMitchellA,
    LinearApproxMitchellB1,
    OutlierAwareLinear,
    Params4bit,
    StableEmbedding,
    SwitchBackLinearBnb,
    Linear4bitFakeQuantAct
)
from .triton_based_modules import (
    StandardLinear,
    SwitchBackLinear,
    SwitchBackLinearGlobal,
    SwitchBackLinearVectorwise,
)
