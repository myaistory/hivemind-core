# 💀 HIVEMIND SKILL PROTOCOL (AIP)
# Parses and validates external skill.md definitions.
class SkillParser:
    def validate_protocol(self, version):
        return version in ['1.2.6', '1.2.8']
