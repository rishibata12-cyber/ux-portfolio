import re

with open('css/style.css', 'r') as f:
    content = f.read()

# Replace specific warm hex codes with monochrome variables
replacements = {
    r'#[0-9A-Fa-f]{6}': {
        '#FDF4F2': 'var(--color-background-primary)',
        '#F2F7F5': 'var(--color-background-primary)',
        '#E07A5F': 'var(--color-text-secondary)',
        '#A64931': 'var(--color-text-secondary)',
        '#662B1C': 'var(--color-text-primary)',
        '#81B29A': 'var(--color-text-secondary)',
        '#4B7863': 'var(--color-text-secondary)',
        '#2A4538': 'var(--color-text-primary)',
        '#F4C4B7': 'var(--color-border-primary)',
        '#C0D8CD': 'var(--color-border-primary)',
    }
}

for pattern, replace_dict in replacements.items():
    for hex_code, var in replace_dict.items():
        content = re.sub(re.escape(hex_code), var, content, flags=re.IGNORECASE)

with open('css/style.css', 'w') as f:
    f.write(content)

print("Colors updated!")
