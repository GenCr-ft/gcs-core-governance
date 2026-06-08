// Gencraft Standard commitlint.config.js (v1.2 - Approved)
// SSoT: gcs-core-governance/commitlint.config.js

module.exports = {
  extends: ['@commitlint/config-conventional'],

  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'style',
        'refactor',
        'perf',
        'test',
        'build',
        'ci',
        'chore',
        'revert',
      ],
    ],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'header-max-length': [2, 'always', 100],
    'body-leading-blank': [1, 'always'],
    'body-max-line-length': [1, 'always', 100],
    'footer-leading-blank': [1, 'always'],
    'footer-max-line-length': [1, 'always', 100],
    'signed-off-by': [0, 'always', 'Signed-off-by:'],
  },
};
