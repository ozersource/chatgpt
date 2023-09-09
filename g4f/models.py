from g4f import Provider
class Model:
	class model:
		name: str
		base_provider: str
		best_provider: str
	class gpt_4_0613:
		name: str = 'gpt-4-0613'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_4_0314:
		name: str = 'gpt-4-0314'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_4_32k_0613:
		name: str = 'gpt-4-32k-0613'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_4_32k_0314:
		name: str = 'gpt-4-32k-0314'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_35_turbo_0613:
		name: str = 'gpt-3.5-turbo-0613'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_35_turbo_0301:
		name: str = 'gpt-3.5-turbo-0301'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_35_turbo_16k_0613:
		name: str = 'gpt-3.5-turbo-16k-0613'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class gpt_35_turbo_16k_0301:
		name: str = 'gpt-3.5-turbo-16k-0301'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class llama_2_70b_chat:
		name: str = 'llama-2-70b-chat'
		base_provider: str = 'hugging-chat-llama'
		best_provider: Provider.Provider = Provider.Chimera
	class code_llama_34b_instruct:
		name: str = 'code-llama-34b-instruct'
		base_provider: str = 'hugging-chat-llama'
		best_provider: Provider.Provider = Provider.Chimera
	class oasst_sft_6_llama_30b:
		name: str = 'oasst-sft-6-llama-30b'
		base_provider: str = 'hugging-chat-llama'
		best_provider: Provider.Provider = Provider.Chimera
	class claude_2:
		name: str = 'claude-2'
		base_provider: str = 'anthropic-claude'
		best_provider: Provider.Provider = Provider.Chimera
	class claude_instant:
		name: str = 'claude-instant'
		base_provider: str = 'anthropic-claude'
		best_provider: Provider.Provider = Provider.Chimera
	class midjourney:
		name: str = 'midjourney'
		base_provider: str = 'midjourney'
		best_provider: Provider.Provider = Provider.Chimera
	class sdxl:
		name: str = 'sdxl'
		base_provider: str = 'stabilityai'
		best_provider: Provider.Provider = Provider.Chimera
	class kandinsky_22:
		name: str = 'kandinsky-2.2'
		base_provider: str = 'sberbank'
		best_provider: Provider.Provider = Provider.Chimera
	class kandinsky_2:
		name: str = 'kandinsky-2'
		base_provider: str = 'sberbank'
		best_provider: Provider.Provider = Provider.Chimera
	class dall_e:
		name: str = 'dall-e'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class stable_diffusion_21:
		name: str = 'stable-diffusion-2.1'
		base_provider: str = 'stabilityai'
		best_provider: Provider.Provider = Provider.Chimera
	class stable_diffusion_15:
		name: str = 'stable-diffusion-1.5'
		base_provider: str = 'stabilityai'
		best_provider: Provider.Provider = Provider.Chimera
	class deepfloyd_if:
		name: str = 'deepfloyd-if'
		base_provider: str = 'deepfloyd'
		best_provider: Provider.Provider = Provider.Chimera
	class material_diffusion:
		name: str = 'material-diffusion'
		base_provider: str = 'yes'
		best_provider: Provider.Provider = Provider.Chimera
	class text_embedding_ada_002:
		name: str = 'text-embedding-ada-002'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class text_moderation_stable:
		name: str = 'text-moderation-stable'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class text_moderation_latest:
		name: str = 'text-moderation-latest'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
	class whisper_1:
		name: str = 'whisper-1'
		base_provider: str = 'openai'
		best_provider: Provider.Provider = Provider.Chimera
class ModelUtils:
	convert: dict = {
		'gpt-4-0613':Model.gpt_4_0613,
		'gpt-4-0314':Model.gpt_4_0314,
		'gpt-4-32k-0613':Model.gpt_4_32k_0613,
		'gpt-4-32k-0314':Model.gpt_4_32k_0314,
		'gpt-3.5-turbo-0613':Model.gpt_35_turbo_0613,
		'gpt-3.5-turbo-0301':Model.gpt_35_turbo_0301,
		'gpt-3.5-turbo-16k-0613':Model.gpt_35_turbo_16k_0613,
		'gpt-3.5-turbo-16k-0301':Model.gpt_35_turbo_16k_0301,
		'llama-2-70b-chat':Model.llama_2_70b_chat,
		'code-llama-34b-instruct':Model.code_llama_34b_instruct,
		'oasst-sft-6-llama-30b':Model.oasst_sft_6_llama_30b,
		'claude-2':Model.claude_2,
		'claude-instant':Model.claude_instant,
		'midjourney':Model.midjourney,
		'sdxl':Model.sdxl,
		'kandinsky-2.2':Model.kandinsky_22,
		'kandinsky-2':Model.kandinsky_2,
		'dall-e':Model.dall_e,
		'stable-diffusion-2.1':Model.stable_diffusion_21,
		'stable-diffusion-1.5':Model.stable_diffusion_15,
		'deepfloyd-if':Model.deepfloyd_if,
		'material-diffusion':Model.material_diffusion,
		'text-embedding-ada-002':Model.text_embedding_ada_002,
		'text-moderation-stable':Model.text_moderation_stable,
		'text-moderation-latest':Model.text_moderation_latest,
		'whisper-1':Model.whisper_1,
	}
