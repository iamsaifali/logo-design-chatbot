def get_logo_prompt(logo_type):
    prompts = {
        "Wordmark (Logotype)": "Design a minimalist, elegant wordmark logo using a clean sans-serif font. The logo should feature a harmonious color palette that reflects emotions like [desired emotions] and brand values like [brand values]. Include precise typography and make use of negative space for a refined and memorable design.",
        
        "Lettermark (Monogram)": "Create a sophisticated lettermark logo featuring interlocking initials or a monogram. Explore unique combinations of font styles, varying weights, and layouts to produce a balanced and visually pleasing design.",
        
        "Pictorial Mark (Brandmark or Symbol)": "Develop an iconic pictorial mark symbolizing the brand's essence. Use simple yet recognizable abstract shapes, symbols, or illustrations that can be scaled without losing their impact.",
        
        "Abstract Mark": "Design a bold abstract mark logo with striking lines, shapes, or patterns. Incorporate vivid color combinations and textures to produce a memorable symbol with a visually dynamic presence.",
        
        "Mascot Logo": "Create an engaging mascot logo that conveys the brand’s personality. Design a mascot character with relatable traits tailored to the target audience's preferences, making sure it reflects their values and interests.",
        
        "Combination Mark": "Develop a cohesive combination logo, integrating a wordmark and pictorial mark. Ensure both elements complement each other, using consistent color schemes and layouts to create a visually appealing and unified logo.",
        
        "Emblem Logo": "Design a timeless emblem logo using a shield or circular frame. Include intricate decorative elements, stylish typography, and a color scheme that reflects the brand's history and traditional values.",
        
        "Dynamic Logo": "Create a logo that evokes motion or dynamic features. Use elements like gradients, animated visuals, or color transitions to give the design a sense of movement and innovation."
    }
    return prompts.get(logo_type, "Design a versatile logo that is visually appealing, memorable, and suitable for the brand’s identity.")
