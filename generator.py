import replicate
import os

os.environ['REPLICATE_API_TOKEN'] = '1d0075d020cb454e861cc2ba20eb13db7b04ead5'
model = replicate.models.get("nateraw/stable-diffusion-videos")
version = model.versions.get("2d87f0f8bc282042002f8d24458bbf588eee5e8d8fffb6fbb10ed48d1dac409e")

# https://replicate.com/nateraw/stable-diffusion-videos/versions/2d87f0f8bc282042002f8d24458bbf588eee5e8d8fffb6fbb10ed48d1dac409e#input
inputs = {
    # Input prompts, separate each prompt with '|'.
    'prompts': "a cat | a dog | a horse",

    # Random seed, separated with '|' to use different seeds for each of
    # the prompt provided above. Leave blank to randomize the seed.
    # 'seeds': ...,

    # Choose the scheduler
    'scheduler': "klms",

    # Number of denoising steps for each image generated from the prompt
    # Range: 1 to 500
    'num_inference_steps': 50,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 7.5,

    # Steps for generating the interpolation video. Recommended to set to
    # 3 or 5 for testing, then up it to 60-200 for better results.
    'num_steps': 50,

    # Frame rate for the video.
    # Range: 5 to 60
    'fps': 15,
}

# https://replicate.com/nateraw/stable-diffusion-videos/versions/2d87f0f8bc282042002f8d24458bbf588eee5e8d8fffb6fbb10ed48d1dac409e#output-schema
output = version.predict(**inputs)
print(type(output))
print("Printing output")
print(output)